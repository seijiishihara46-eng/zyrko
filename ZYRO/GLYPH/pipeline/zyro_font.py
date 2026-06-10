"""
Build the Zyro font (U+E000) from the canonical outline.
Pure-Python: shapely (via zyro_outline) + fontTools.
Run: python zyro_font.py [flip]  ->  writes ../dist/Zyrko.ttf and ../dist/Zyrko.woff2

'flip' inverts contour winding (verification toggle).
"""
import sys
from pathlib import Path
from shapely.geometry.polygon import orient
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

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


def build_glyph():
    pen = TTGlyphPen(None)
    outer_cw = not FLIP
    for p in polys:
        po = orient(p, 1.0)
        emit_ring(pen, list(po.exterior.coords), want_cw=outer_cw)
        for hole in po.interiors:
            emit_ring(pen, list(hole.coords), want_cw=(not outer_cw))
    return pen.glyph()


xs = [round(x * SCALE) for p in polys for x, y in p.exterior.coords]
glyph_zyro = build_glyph()
empty = TTGlyphPen(None).glyph()

fb = FontBuilder(UPM, isTTF=True)
fb.setupGlyphOrder([".notdef", "space", "zyro"])
fb.setupCharacterMap({0x20: "space", 0xE000: "zyro"})
fb.setupGlyf({".notdef": empty, "space": empty, "zyro": glyph_zyro})
adv = int(200 * SCALE)
fb.setupHorizontalMetrics({".notdef": (adv, 0), "space": (adv, 0), "zyro": (adv, min(xs))})
fb.setupHorizontalHeader(ascent=800, descent=-200)
fb.setupNameTable({
    "familyName": "Zyrko", "styleName": "Regular",
    "fullName": "Zyrko Regular", "psName": "Zyrko-Regular",
    "version": "1.0",
    "copyright": "Zyrko glyph U+E000 (canonical v2.5, frozen 2026-06-10)"})
fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800, usWinDescent=200)
fb.setupPost()

fb.save(str(DIST / "Zyrko.ttf"))
fb.font.flavor = "woff2"
fb.font.save(str(DIST / "Zyrko.woff2"))
print(f"built {DIST/'Zyrko.ttf'} / Zyrko.woff2 | parts={len(polys)} adv={adv} xmin={min(xs)} flip={FLIP}")
