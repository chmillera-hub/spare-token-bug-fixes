# Getting coordinates along the paths of one colour in an SVG file

## Link to the original question

https://discuss.python.org/t/104239

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with the Python library svgpathtools on a small made-up SVG file and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 8 October 2025 somebody asked on the Python help forum how to get the coordinates of the path objects of one colour in an SVG drawing.
Matching pixel colours in a PNG picture had given jagged edges so the asker moved to SVG paths and tried to turn each curve segment into a polynomial and then search the polynomial for a colour which returned nothing useful.
The post had zero replies when the forum list was read on 12 November 2026.

## What went wrong in the posted program

A polynomial of a curve segment holds the formula of the curve and holds no colour so comparing the polynomial with a colour finds nothing.
The colour of an SVG path lives in the attributes of the path (inside the style text or in a separate stroke or fill attribute) and the coordinates come from asking the path for points along its length.

## What the test shows

The test file had a green path made of a curve and a straight line and a red path and a second green path that stored the colour in a separate attribute with capital letters.

- Filtering on the colour #00ff00 kept the two green paths and skipped the red path.
- Each green path returned 85 points from the first point to the last point of the path.
- The largest gap between neighbouring points was under 1 unit because the points were spaced evenly along the length of the path.

## Best-guess answer

The following functions worked in the test:

def colour_of(attribs, key="stroke"):
    m = re.search(key + r"\s*:\s*([^;]+)", attribs.get("style", ""))
    value = m.group(1) if m else attribs.get(key, "")
    return value.strip().lower()

def points_on(path, step=1.0):
    n = max(2, int(np.ceil(path.length() / step)) + 1)
    pts = [path.point(path.ilength(s)) for s in np.linspace(0, path.length(), n)]
    return np.array([(p.real, p.imag) for p in pts])

paths, attributes, svg_attributes = svg2paths2(filename)
green = [points_on(p) for p, a in zip(paths, attributes) if colour_of(a) == "#00ff00"]

Using key="fill" in place of key="stroke" filters on the fill colour.
The library stores every point as one complex number so the x value is the real part and the y value is the imaginary part.
Colours written as names (such as "lime") or as rgb(0,255,0) need an extra conversion step that the test did not cover.

The test file named svg_by_colour.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
