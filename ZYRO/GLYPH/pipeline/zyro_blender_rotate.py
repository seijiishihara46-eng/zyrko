"""
Zyro Metal — turntable rotation animation (Blender 4.4 headless).
Builds the silver chrome glyph (same as zyro_blender.py) and spins it 360 deg
around the vertical axis, rendering a seamless-loop PNG sequence.

Run:
  "C:\\Program Files\\Blender Foundation\\Blender 4.4\\blender.exe" \
    --background --python zyro_blender_rotate.py

Output: ../3d/frames/zyro_####.png   (then encode with ffmpeg, see footer)
"""
import bpy, addon_utils, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.realpath(__file__))
SVG  = os.path.normpath(os.path.join(HERE, "..", "dist", "zyro-glyph-outline.svg"))
OUT  = os.path.normpath(os.path.join(HERE, "..", "3d", "frames"))
os.makedirs(OUT, exist_ok=True)

FRAMES = 60          # 30 fps -> 2.0 s seamless loop
SAMPLES = 48
RES = 720

bpy.ops.wm.read_factory_settings(use_empty=True)

# ---- import SVG curves ----
try: addon_utils.enable("io_curve_svg", default_set=True)
except Exception as e: print("addon note:", e)
before = set(bpy.data.objects)
for op in ("import_curve.svg", "wm.svg_import"):
    try:
        mod, fn = op.split("."); getattr(getattr(bpy.ops, mod), fn)(filepath=SVG); break
    except Exception as e: print("import", op, "failed:", e)
curves = [o for o in bpy.data.objects if o not in before and o.type == "CURVE"]
for c in curves:
    c.data.dimensions = "2D"; c.data.fill_mode = "BOTH"

for o in bpy.data.objects: o.select_set(False)
for c in curves: c.select_set(True)
bpy.context.view_layer.objects.active = curves[0]
bpy.ops.object.join()
glyph = bpy.context.view_layer.objects.active; glyph.name = "ZyroGlyph"
bpy.ops.object.convert(target="MESH")

# center + scale
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS"); glyph.location = (0, 0, 0)
bb = [glyph.matrix_world @ Vector(c) for c in glyph.bound_box]
width = max(v.x for v in bb) - min(v.x for v in bb)
s = 2.0 / width if width else 1.0
glyph.scale = (s, s, s); bpy.ops.object.transform_apply(scale=True)
glyph.scale.y *= -1; bpy.ops.object.transform_apply(scale=True)
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS"); glyph.location = (0, 0, 0)

# fix normals (negative scale flipped them)
bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.normals_make_consistent(inside=False); bpy.ops.object.mode_set(mode="OBJECT")

# extrude + bevel
solid = glyph.modifiers.new("solid", "SOLIDIFY"); solid.thickness = 0.18; solid.offset = 0.0
bev = glyph.modifiers.new("bevel", "BEVEL"); bev.width = 0.012; bev.segments = 3
bpy.ops.object.shade_smooth()

# silver chrome material (replace the SVG-assigned black material)
mat = bpy.data.materials.new("ZyroMetal"); mat.use_nodes = True
bsdf = next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
bsdf.inputs["Base Color"].default_value = (0.80, 0.81, 0.84, 1)
bsdf.inputs["Metallic"].default_value = 1.0
bsdf.inputs["Roughness"].default_value = 0.30
glyph.data.materials.clear(); glyph.data.materials.append(mat)
for poly in glyph.data.polygons: poly.material_index = 0

# stand up (face -Y, vertical axis = world Z)
glyph.rotation_euler = (math.radians(90), 0, 0); bpy.ops.object.transform_apply(rotation=True)

# ---- turntable animation: spin around world Z ----
scene = bpy.context.scene
scene.frame_start = 1; scene.frame_end = FRAMES
for f in range(1, FRAMES + 1):
    glyph.rotation_euler = (0, 0, 2 * math.pi * (f - 1) / FRAMES)   # 1->0, last->just before 360
    glyph.keyframe_insert("rotation_euler", frame=f)
for fc in glyph.animation_data.action.fcurves:
    for kp in fc.keyframe_points: kp.interpolation = "LINEAR"

# ---- world / lights / camera (same studio as the still) ----
world = bpy.data.worlds.new("W"); scene.world = world; world.use_nodes = True
wbg = next((n for n in world.node_tree.nodes if n.type == "BACKGROUND"), None)
wbg.inputs[0].default_value = (0.012, 0.012, 0.015, 1)

def area(name, loc, rot, size, energy, color=(1, 1, 1)):
    l = bpy.data.lights.new(name, "AREA"); l.size = size; l.energy = energy; l.color = color
    o = bpy.data.objects.new(name, l); o.location = loc; o.rotation_euler = rot
    bpy.context.collection.objects.link(o)
area("softbox", (0.0, -5.6, 0.4), (math.radians(90), 0, 0), 11.0, 2600)
area("key",  (-2.6, -3.2, 2.4), (math.radians(58), 0, math.radians(-38)), 3.2, 2600)
area("rim",  ( 3.0, -2.2, 1.8), (math.radians(70), 0, math.radians(52)),  2.4, 2200, (0.78, 0.85, 1.0))
area("top",  ( 0.0, -1.6, 3.2), (math.radians(20), 0, 0),                 3.5, 1600)

target = bpy.data.objects.new("target", None); target.location = (0, 0, 0)
bpy.context.collection.objects.link(target)
cam_d = bpy.data.cameras.new("cam"); cam = bpy.data.objects.new("cam", cam_d)
bpy.context.collection.objects.link(cam)
cam.location = (-1.5, -3.9, 1.15); cam_d.lens = 78
trk = cam.constraints.new("TRACK_TO"); trk.target = target
trk.track_axis = "TRACK_NEGATIVE_Z"; trk.up_axis = "UP_Y"
scene.camera = cam

# ---- render ----
scene.render.engine = "CYCLES"
try: scene.cycles.device = "GPU"
except Exception: pass
scene.cycles.samples = SAMPLES
try: scene.cycles.use_denoising = True
except Exception: pass
scene.render.resolution_x = RES; scene.render.resolution_y = RES
scene.render.film_transparent = False
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = os.path.join(OUT, "zyro_")
bpy.ops.render.render(animation=True)
print("RENDERED FRAMES ->", OUT)

# ---- encode (run after) ----
# mp4 : ffmpeg -framerate 30 -i zyro_%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 zyro-metal-rotate.mp4
# webm: ffmpeg -framerate 30 -i zyro_%04d.png -c:v libvpx-vp9 -b:v 0 -crf 32 zyro-metal-rotate.webm
# gif : ffmpeg -framerate 30 -i zyro_%04d.png -vf "scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" zyro-metal-rotate.gif
