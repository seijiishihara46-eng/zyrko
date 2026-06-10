"""
Zyro 3D / Metal — Blender headless build.
Imports the fill-only outline SVG (Orbit as counters), extrudes it into a
metal medallion, lights it as dark chrome, and renders a still.

Run:
  "C:\\Program Files\\Blender Foundation\\Blender 4.4\\blender.exe" --background --python zyro_blender.py

Outputs (../3d/):
  zyro-metal.png      rendered still
  zyro-glyph.blend    scene file
"""
import bpy, addon_utils, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.realpath(__file__))
SVG  = os.path.normpath(os.path.join(HERE, "..", "dist", "zyro-glyph-outline.svg"))
OUT  = os.path.normpath(os.path.join(HERE, "..", "3d"))
os.makedirs(OUT, exist_ok=True)

# ---- clean scene ----
bpy.ops.wm.read_factory_settings(use_empty=True)

# ---- import SVG as curves ----
try:
    addon_utils.enable("io_curve_svg", default_set=True)
except Exception as e:
    print("addon enable note:", e)

before = set(bpy.data.objects)
imported = False
for op in ("import_curve.svg", "wm.svg_import"):
    try:
        mod, fn = op.split(".")
        getattr(getattr(bpy.ops, mod), fn)(filepath=SVG)
        imported = True
        break
    except Exception as e:
        print("import op", op, "failed:", e)
if not imported:
    raise SystemExit("SVG import failed")

new = [o for o in bpy.data.objects if o not in before]
curves = [o for o in new if o.type == "CURVE"]
print("imported curves:", len(curves))

# fill the curves so conversion yields solid faces with counters
for c in curves:
    c.data.dimensions = "2D"
    c.data.fill_mode = "BOTH"

# ---- join + convert to mesh ----
for o in bpy.data.objects:
    o.select_set(False)
for c in curves:
    c.select_set(True)
bpy.context.view_layer.objects.active = curves[0]
bpy.ops.object.join()
glyph = bpy.context.view_layer.objects.active
glyph.name = "ZyroGlyph"
bpy.ops.object.convert(target="MESH")

# ---- recenter + scale to target width ----
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
glyph.location = (0, 0, 0)
bb = [glyph.matrix_world @ Vector(c) for c in glyph.bound_box]
width = max(v.x for v in bb) - min(v.x for v in bb)
target_w = 2.0
s = target_w / width if width else 1.0
glyph.scale = (s, s, s)
bpy.ops.object.transform_apply(scale=True, location=False, rotation=False)

# flip so it faces up the Z axis nicely (SVG y-down -> mirror Y)
glyph.scale.y *= -1
bpy.ops.object.transform_apply(scale=True)
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
glyph.location = (0, 0, 0)

# fix normals (the negative-Y scale flipped them) before extruding
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.object.mode_set(mode="OBJECT")

# ---- extrude (solidify) ----
solid = glyph.modifiers.new("solid", "SOLIDIFY")
solid.thickness = 0.18
solid.offset = 0.0
bev = glyph.modifiers.new("bevel", "BEVEL")
bev.width = 0.012
bev.segments = 3
bpy.ops.object.shade_smooth()

# ---- dark chrome material ----
mat = bpy.data.materials.new("ZyroMetal")
mat.use_nodes = True
bsdf = next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
# polished silver chrome (matches the figure's silver face), reads bright on dark bg
bsdf.inputs["Base Color"].default_value = (0.80, 0.81, 0.84, 1)
bsdf.inputs["Metallic"].default_value = 1.0
bsdf.inputs["Roughness"].default_value = 0.30
glyph.data.materials.clear()   # drop the black material the SVG import assigned
glyph.data.materials.append(mat)
for poly in glyph.data.polygons:
    poly.material_index = 0

# stand glyph up (face the camera on +Y) : rotate so its face plane is vertical
glyph.rotation_euler = (math.radians(90), 0, 0)
bpy.ops.object.transform_apply(rotation=True)

# ---- world (dark, subtle so chrome has something to reflect) ----
world = bpy.data.worlds.new("W"); bpy.context.scene.world = world
world.use_nodes = True
wbg = next((n for n in world.node_tree.nodes if n.type == "BACKGROUND"), None)
wbg.inputs[0].default_value = (0.012, 0.012, 0.015, 1)
wbg.inputs[1].default_value = 1.0

# ---- lights (studio: key + rim + fill as bright cards for metal streaks) ----
def area(name, loc, rot, size, energy, color=(1,1,1)):
    l = bpy.data.lights.new(name, "AREA"); l.size = size; l.energy = energy; l.color = color
    o = bpy.data.objects.new(name, l); o.location = loc; o.rotation_euler = rot
    bpy.context.collection.objects.link(o); return o
# big front softbox (reflected by the chrome face -> reads bright silver), out of frame
area("softbox", (0.0, -5.6, 0.4), (math.radians(90), 0, 0), 11.0, 2600)
area("key",  (-2.6, -3.2, 2.4), (math.radians(58), 0, math.radians(-38)), 3.2, 2600)
area("rim",  ( 3.0, -2.2, 1.8), (math.radians(70), 0, math.radians(52)),  2.4, 2200, (0.78,0.85,1.0))
area("top",  ( 0.0, -1.6, 3.2), (math.radians(20), 0, 0),                 3.5, 1600)

# ---- camera (3/4 view to show depth + bevel highlights), tracks origin ----
target = bpy.data.objects.new("target", None); target.location = (0, 0, 0)
bpy.context.collection.objects.link(target)
cam_d = bpy.data.cameras.new("cam"); cam = bpy.data.objects.new("cam", cam_d)
bpy.context.collection.objects.link(cam)
cam.location = (-1.5, -3.9, 1.15)
cam_d.lens = 78
trk = cam.constraints.new("TRACK_TO"); trk.target = target
trk.track_axis = "TRACK_NEGATIVE_Z"; trk.up_axis = "UP_Y"
bpy.context.scene.camera = cam

# ---- render settings ----
sc = bpy.context.scene
sc.render.engine = "CYCLES"
try: sc.cycles.device = "GPU"
except Exception: pass
sc.cycles.samples = 96
try: sc.cycles.use_denoising = True
except Exception: pass
sc.render.resolution_x = 1000
sc.render.resolution_y = 1000
sc.render.film_transparent = False
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = os.path.join(OUT, "zyro-metal.png")

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "zyro-glyph.blend"))
bpy.ops.render.render(write_still=True)
print("RENDERED:", sc.render.filepath)
