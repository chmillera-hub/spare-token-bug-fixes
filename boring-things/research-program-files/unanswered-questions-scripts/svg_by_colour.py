# Gets x and y coordinates along the paths of one colour in an SVG file (Python forum topic 104239)
import re, numpy as np, svgpathtools
from svgpathtools import svg2paths2
print("svgpathtools", getattr(svgpathtools, "__version__", "version not exposed"))
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
<path id="path1" style="fill:none;stroke:#00ff00;stroke-width:1" d="M 10,10 C 20,0 40,0 50,10 L 90,10"/>
<path id="path2" style="fill:none;stroke:#ff0000;stroke-width:1" d="M 10,50 L 90,50"/>
<path id="path3" stroke="#00FF00" fill="none" d="M 10,80 Q 50,60 90,80"/>
</svg>'''
open("test.svg", "w").write(svg)

def colour_of(attribs, key="stroke"):
    # the colour can sit in a style string ("stroke:#00ff00") or in its own attribute (stroke="#00ff00")
    m = re.search(key + r"\s*:\s*([^;]+)", attribs.get("style", ""))
    value = m.group(1) if m else attribs.get(key, "")
    return value.strip().lower()

def points_on(path, step=1.0):
    # evenly spaced points along the whole path, about one point per "step" units of length
    n = max(2, int(np.ceil(path.length() / step)) + 1)
    pts = [path.point(path.ilength(s)) for s in np.linspace(0, path.length(), n)]
    return np.array([(p.real, p.imag) for p in pts])

paths, attributes, svg_attributes = svg2paths2("test.svg")
wanted = "#00ff00"
for path, attribs in zip(paths, attributes):
    if colour_of(attribs) != wanted:
        continue
    xy = points_on(path)
    gaps = np.hypot(*np.diff(xy, axis=0).T)
    print(f"{attribs['id']}: {len(xy)} points | first {np.round(xy[0], 3)} | last {np.round(xy[-1], 3)} | largest gap between neighbours {gaps.max():.3f}")
    print("   segment types:", [type(seg).__name__ for seg in path])
print("paths skipped because of a different colour:", [a["id"] for a in attributes if colour_of(a) != wanted])
