"""
Build the Zyro font (U+E000) from the canonical outline.
Pure-Python: shapely (via zyro_outline) + fontTools.
Run: python zyro_font.py [flip]
  -> ../dist/Zyrko.ttf, ../dist/Zyrko.woff2  (TrueType / glyf)
  -> ../dist/Zyrko.otf                       (OpenType / CFF)

'flip' inverts contour winding (verification toggle).
"""
import sys
from pathlib import Path
from shapely.geometry.polygon import orient
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.t2CharStringPen import T2CharStringPen

from zyro_outline import build as build_outline   # same folder

BASE = Path(__file__).resolve().parent.parent     # ZYRO/GLYPH
DIST = BASE / "dist"
DIST.mkdir(exist_ok=True)

UPM = 1000
SCALE = 5.0          # 200x100 viewBox -> 1000x500
SIMPLIFY = 0.25      # node reduction tolerance (viewBox units)
FLIP = (len(sys.argv) > 1 and sys.argv[1] == "flip")

glyph_geom = build_outline().simplify(SIMPLIFY)
polys = list(glyph_geom.geoms) if glyph_geom.geom_type == "MultiPolygon" else [glyph_geom]


def to_font(x, y):
    return (round(x * SCALE), round((100 - y) * SCALE))   # flip y for font (y-up)


def shoelace(coords):
    a = 0
    for i in range(len(coords) - 1):
        x0, y0 = coords[i]; x1, y1 = coords[i + 1]
        a += x0 * y1 - x1 * y0
    return a / 2


def emit_ring(pen, coords, want_cw):
    fc = [to_font(x, y) for x, y in coords]
    if fc[0] == fc[-1]:
        fc = fc[:-1]
    is_cw = shoelace(fc + [fc[0]]) < 0
    if is_cw != want_cw:
        fc = fc[::-1]
    pen.moveTo(fc[0])
    for p in fc[1:]:
        pen.lineTo(p)
    pen.closePath()


def draw_glyph(pen, outer_cw):
    """Pen-agnostic: works for TTGlyphPen and T2CharStringPen alike."""
    for p in polys:
        po = orient(p, 1.0)
        emit_ring(pen, list(po.exterior.coords), want_cw=outer_cw)
        for hole in po.interiors:
            emit_ring(pen, list(hole.coords), want_cw=(not outer_cw))


adv = int(200 * SCALE)
xs = [round(x * SCALE) for p in polys for x, y in p.exterior.coords]
xmin = min(xs)

NAMES = {
    "familyName": "Zyrko", "styleName": "Regular",
    "fullName": "Zyrko Regular", "psName": "Zyrko-Regular",
    "version": "1.0",
    "copyright": "Zyrko glyph U+E000 (canonical v2.5, frozen 2026-06-10)"}
METRICS = {".notdef": (adv, 0), "space": (adv, 0), "zyro": (adv, xmin)}
ORDER = [".notdef", "space", "zyro"]
CMAP = {0x20: "space", 0xE000: "zyro"}


def finish(fb):
    fb.setupHorizontalMetrics(METRICS)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable(NAMES)
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800, usWinDescent=200)
    fb.setupPost()


# ---- TrueType (glyf): outer contours clockwise ----
tt_pen = TTGlyphPen(None)
draw_glyph(tt_pen, outer_cw=not FLIP)
fb = FontBuilder(UPM, isTTF=True)
fb.setupGlyphOrder(ORDER)
fb.setupCharacterMap(CMAP)
fb.setupGlyf({".notdef": TTGlyphPen(None).glyph(), "space": TTGlyphPen(None).glyph(),
              "zyro": tt_pen.glyph()})
finish(fb)
fb.save(str(DIST / "Zyrko.ttf"))
fb.font.flavor = "woff2"
fb.font.save(str(DIST / "Zyrko.woff2"))

# ---- OpenType (CFF): PostScript winding is opposite -> outer counter-clockwise ----
cff_pen = T2CharStringPen(adv, None)
draw_glyph(cff_pen, outer_cw=bool(FLIP))
charstrings = {
    ".notdef": T2CharStringPen(adv, None).getCharString(),
    "space": T2CharStringPen(adv, None).getCharString(),
    "zyro": cff_pen.getCharString(),
}
fbo = FontBuilder(UPM, isTTF=False)
fbo.setupGlyphOrder(ORDER)
fbo.setupCharacterMap(CMAP)
fbo.setupCFF(NAMES["psName"], {"FullName": NAMES["fullName"], "FamilyName": NAMES["familyName"]},
             charstrings, {})
finish(fbo)
fbo.save(str(DIST / "Zyrko.otf"))

print(f"built Zyrko.ttf / .woff2 / .otf | parts={len(polys)} adv={adv} xmin={xmin} flip={FLIP}")
