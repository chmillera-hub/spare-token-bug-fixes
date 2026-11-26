"""The patch of light that passes through the middle of a Mobius strip.

Straight light shines through the opening in the middle of the strip onto a wall.
The program tilts the strip away from face-on in several directions and records
the shape of the lit patch at every tilt.

Run:  python3 hole_light.py [output_folder]
"""
import json
import sys
import numpy as np
from scipy import ndimage
from scipy.spatial import ConvexHull
from PIL import Image, ImageDraw
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shadow_variety import mobius, raster

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
RES = 240
SCALE = 1.5


def view(V, F, tilt_deg, toward_deg):
    """Shadow picture with the strip tilted tilt_deg away from face-on.
    toward_deg says which part of the strip leans away from the light."""
    t, p = np.radians(tilt_deg), np.radians(toward_deg)
    d = np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
    e1 = np.array([-np.sin(p), np.cos(p), 0.0])
    e2 = np.cross(d, e1)
    P = np.c_[V @ e1, V @ e2]
    return raster(P, F, RES, np.zeros(2), SCALE)


def patch(shadow):
    """The lit patch = the largest bright region fully fenced in by the shadow."""
    lab, n = ndimage.label(~shadow)
    edge = set(lab[0]) | set(lab[-1]) | set(lab[:, 0]) | set(lab[:, -1])
    best, size = None, 0
    for i in range(1, n + 1):
        if i in edge:
            continue
        s = int((lab == i).sum())
        if s > size:
            best, size = lab == i, s
    return best, size


def describe(m):
    ys, xs = np.nonzero(m)
    pix = np.c_[xs, ys].astype(float)
    w = np.sqrt(np.maximum(np.linalg.eigvalsh(np.cov((pix - pix.mean(0)).T)), 1e-9))
    hull = ConvexHull(pix)
    him = Image.new("1", (RES, RES), 0)
    ImageDraw.Draw(him).polygon([tuple(pix[i]) for i in hull.vertices], fill=1, outline=1)
    return {"long_over_short": float(w[1] / w[0]), "fill_of_rubber_band_outline": float(m.sum() / np.array(him).sum())}


if __name__ == "__main__":
    shapes = {"Mobius strip": mobius()}
    table = {}
    for name, (V, F) in shapes.items():
        face_on = patch(view(V, F, 0.5, 0))[1]   # half a degree off face-on so an edge-on band still draws a closed ring
        rows = {}
        for toward in range(0, 360, 30):
            closes, series = None, []
            for tilt in range(0, 91, 2):
                m, size = patch(view(V, F, max(tilt, 0.5), toward))
                if size < 15:
                    closes = tilt
                    break
                d = describe(m)
                series.append({"tilt": tilt, "area_compared_with_face_on": size / face_on, **d})
            rows[toward] = {"patch_closes_at_tilt": closes, "series": series}
        table[name] = rows
        print(name, {k: v["patch_closes_at_tilt"] for k, v in rows.items()}, flush=True)
        for toward in (0, 90, 270):
            print("  toward", toward, [(s["tilt"], round(s["area_compared_with_face_on"], 2), round(s["long_over_short"], 1),
                                       round(s["fill_of_rubber_band_outline"], 2)) for s in rows[toward]["series"][::5]])
    json.dump(table, open(OUT + "/hole_light_results.json", "w"), indent=1)

    # picture: rows = which part leans away, columns = tilt
    V, F = shapes["Mobius strip"]
    tilts = [0, 20, 40, 55, 70]
    rows = [(0, "Tilting end over end (the flat-lying part swings toward the light)"),
            (90, "Tilting sideways one way"),
            (270, "Tilting sideways the other way")]
    fig = plt.figure(figsize=(7.2, 2.05 * len(rows) + 0.9), dpi=150)
    fig.suptitle("Light through the middle of a Mobius strip as the strip tilts", fontsize=13.5, y=0.995)
    gs = fig.add_gridspec(len(rows), len(tilts), hspace=0.38, wspace=0.04, top=0.90, bottom=0.01, left=0.02, right=0.98)
    for r, (toward, label) in enumerate(rows):
        for c, tilt in enumerate(tilts):
            sh = view(V, F, tilt, toward)
            m, size = patch(sh)
            img = np.zeros((RES, RES, 3))
            img[sh] = 0.28                      # the strip, shown dim for reference
            if m is not None and size >= 15:
                img[m] = (1.0, 0.92, 0.45)      # the lit patch
            ax = fig.add_subplot(gs[r, c]); ax.axis("off"); ax.imshow(img, interpolation="nearest")
            ax.text(0.5, -0.06, "tilt %d" % tilt, transform=ax.transAxes, ha="center", va="top", fontsize=9)
            if c == 0:
                ax.set_title(label, fontsize=10.5, loc="left", pad=4)
    fig.savefig(OUT + "/light-through-mobius.png", facecolor="white")
