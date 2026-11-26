"""Shadow variety test.

Casts the shadow of each shape under parallel light (like sunlight) from many
directions spread evenly over a sphere and counts how many of the shadows are
different from one another after allowing free rotation and mirror flips of the
shadow on the wall and after scaling every shadow to the same size.

Run:  python3 shadow_variety.py  [output_folder]
"""
import json
import sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
from scipy.spatial import ConvexHull

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
BIG = 160      # raster used for holes and dents
RES = 48       # raster used for comparing shadows
N_DIR = 2000   # light directions per shape
EPS = [0.15, 0.25, 0.35]   # how different two shadows must be to count as different


# ---------------------------------------------------------------- shapes
def grid_mesh(fn, nu, nv, u0, u1, v0, v1):
    us = np.linspace(u0, u1, nu + 1)
    vs = np.linspace(v0, v1, nv + 1)
    V = np.array([fn(u, v) for u in us for v in vs])
    F = []
    for i in range(nu):
        for j in range(nv):
            a = i * (nv + 1) + j
            b = a + 1
            c = a + nv + 1
            d = c + 1
            F += [(a, b, c), (b, d, c)]
    return V, np.array(F)


def mobius(w=0.4):
    f = lambda u, v: ((1 + v * np.cos(u / 2)) * np.cos(u),
                      (1 + v * np.cos(u / 2)) * np.sin(u),
                      v * np.sin(u / 2))
    return grid_mesh(f, 96, 6, 0, 2 * np.pi, -w, w)


def loop(w=0.4):
    f = lambda u, v: (np.cos(u), np.sin(u), v)
    return grid_mesh(f, 96, 4, 0, 2 * np.pi, -w, w)


def sphere():
    f = lambda u, v: (np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v))
    return grid_mesh(f, 32, 16, 0, 2 * np.pi, 0, np.pi)


def disk():
    t = np.linspace(0, 2 * np.pi, 97)[:-1]
    V = np.vstack([[0, 0, 0], np.c_[np.cos(t), np.sin(t), 0 * t]])
    F = [(0, 1 + i, 1 + (i + 1) % 96) for i in range(96)]
    return V, np.array(F)


def square():
    V = np.array([[-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0]], float)
    return V, np.array([(0, 1, 2), (0, 2, 3)])


def cube():
    V = np.array([[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], float)
    return V, ConvexHull(V).simplices


def rock():
    rng = np.random.default_rng(7)
    V = rng.normal(size=(14, 3)) * [1.0, 0.8, 0.6]
    return V, ConvexHull(V).simplices


def stretched(shape, k=1.6):
    V, F = shape
    V = V.copy()
    V[:, 0] *= k
    return V, F


# ---------------------------------------------------------------- shadows
def directions(n):
    i = np.arange(n) + 0.5
    z = 1 - 2 * i / n
    r = np.sqrt(1 - z * z)
    ph = i * np.pi * (3 - np.sqrt(5))
    return np.c_[r * np.cos(ph), r * np.sin(ph), z]


def project(V, d):
    a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(d, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(d, e1)
    return np.c_[V @ e1, V @ e2]


def raster(P, F, res, centre, scale, angle=0.0):
    c, s = np.cos(angle), np.sin(angle)
    Q = (P - centre) @ np.array([[c, -s], [s, c]])
    Q = Q / scale * (res / 2 * 0.92) + res / 2
    im = Image.new("1", (res, res), 0)
    dr = ImageDraw.Draw(im)
    for tri in F:
        dr.polygon([tuple(Q[k]) for k in tri], fill=1, outline=1)
    return np.array(im, dtype=bool)


def shadow(V, F, d, res=RES, want_stats=False):
    return shadow_P(project(V, d), F, res, want_stats)


def shadow_P(P, F, res=RES, want_stats=False):
    c0 = (P.max(0) + P.min(0)) / 2
    s0 = np.linalg.norm(P - c0, axis=1).max() + 1e-9
    big = raster(P, F, BIG, c0, s0)
    ys, xs = np.nonzero(big)
    pix = np.c_[xs, ys].astype(float)
    cen = pix.mean(0)
    cov = np.cov((pix - cen).T) if len(pix) > 2 else np.eye(2)
    w, vec = np.linalg.eigh(cov)
    ang = np.arctan2(vec[1, 1], vec[0, 1])        # direction of the long axis
    rad = np.linalg.norm(pix - cen, axis=1).max() + 0.5
    k = s0 / (BIG / 2 * 0.92)                     # world units per pixel
    centre = c0 + (cen - BIG / 2) * k
    small = raster(P, F, res, centre, rad * k, ang)
    if not want_stats:
        return small
    # holes: background pieces that do not touch the frame
    lab, n = ndimage.label(~big)
    edge = set(lab[0]) | set(lab[-1]) | set(lab[:, 0]) | set(lab[:, -1])
    holes = sum(1 for i in range(1, n + 1) if i not in edge and (lab == i).sum() >= 40)
    # dents: how much of the stretched-rubber-band outline is filled
    try:
        hull = ConvexHull(pix)
        him = Image.new("1", (BIG, BIG), 0)
        ImageDraw.Draw(him).polygon([tuple(pix[i]) for i in hull.vertices], fill=1, outline=1)
        solid = big.sum() / max(np.array(him).sum(), 1)
    except Exception:
        solid = 1.0
    # a shadow thinner than a few pixels cannot be checked for dents reliably
    thin = bool(np.sqrt(max(w[0], 0)) < 4)
    return small, holes, (None if thin else float(min(solid, 1.0)))


# ---------------------------------------------------------------- comparing
def variants(img):
    out = []
    for m in (img, img[:, ::-1]):
        for a in np.arange(0, 360, 7.5):
            if a % 90 == 0:
                r = np.rot90(m, int(a // 90))
            else:
                r = ndimage.rotate(m.astype(np.float32), a, reshape=False, order=1) > 0.5
            out.append(r.ravel())
    return np.array(out, dtype=np.float32)


def dist_to_all(img, X, areas):
    Vv = variants(img)
    inter = X @ Vv.T
    union = areas[:, None] + Vv.sum(1)[None, :] - inter
    return 1 - (inter / np.maximum(union, 1)).max(1)


def farthest_first(imgs, eps_min, cap=500):
    """Pick shadows one at a time, each time taking the shadow least like all
    shadows picked so far.  Returns the picks and the gap at each pick."""
    X = imgs.reshape(len(imgs), -1).astype(np.float32)
    areas = X.sum(1)
    picks, gaps = [0], [1.0]
    mind = dist_to_all(imgs[0], X, areas)
    while len(picks) < cap:
        j = int(mind.argmax())
        if mind[j] <= eps_min:
            break
        picks.append(j)
        gaps.append(float(mind[j]))
        mind = np.minimum(mind, dist_to_all(imgs[j], X, areas))
    return picks, gaps


def count_at(gaps, eps):
    return int(sum(1 for g in gaps if g > eps))


def run(name, shapes, n_total=N_DIR, stats=True):
    """shapes: list of (V, F); the light directions are shared out equally."""
    per = n_total // len(shapes)
    D = directions(per)
    imgs, holes, solids, src = [], [], [], []
    for si, (V, F) in enumerate(shapes):
        for d in D:
            if stats:
                im, h, s = shadow(V, F, d, want_stats=True)
                holes.append(h)
                solids.append(s)
            else:
                im = shadow(V, F, d)
            imgs.append(im)
            src.append((si, d.tolist()))
    imgs = np.array(imgs)
    picks, gaps = farthest_first(imgs, min(EPS))
    res = {"name": name, "shadows_cast": len(imgs),
           "different_shadows": {str(e): count_at(gaps, e) for e in EPS}}
    if stats:
        holes = np.array(holes)
        solids = np.array([x for x in solids if x is not None])
        res.update({
            "share_with_a_hole": float((holes > 0).mean()),
            "most_holes": int(holes.max()),
            "shadows_wide_enough_to_check_for_dents": int(len(solids)),
            "share_with_a_dent": float((solids < 0.90).mean()),
            "deepest_dent_fill": float(solids.min()),
            "hole_counts_seen": sorted(set(int(h) for h in holes)),
        })
    print(json.dumps(res), flush=True)
    return res, imgs, picks, gaps, src


if __name__ == "__main__":
    base = [("sphere", sphere()), ("flat circle", disk()), ("flat square", square()),
            ("cube", cube()), ("lumpy rock", rock()), ("untwisted loop", loop()),
            ("Mobius strip", mobius())]
    results, gallery = [], {}
    for name, sh in base:
        r, imgs, picks, gaps, src = run(name, [sh])
        results.append(r)
        gallery[name] = [imgs[p] for p in picks[:10]]
    np.save(OUT + "/gallery.npy", gallery, allow_pickle=True)

    # does the count settle when fewer light directions are used?
    r, *_ = run("Mobius strip with half as many light directions", [mobius()], n_total=1000, stats=False)
    results.append(r)

    # stretching test: same number of shadows in every pool
    pools = [
        ("flat circle plus stretched circle", [disk(), stretched(disk())]),
        ("flat square plus stretched square", [square(), stretched(square())]),
        ("untwisted loop plus stretched and wider and narrower loops",
         [loop(), stretched(loop()), loop(0.25), loop(0.6)]),
        ("Mobius strip plus stretched and wider and narrower Mobius strips",
         [mobius(), stretched(mobius()), mobius(0.25), mobius(0.6)]),
    ]
    for name, shapes in pools:
        r, *_ = run(name, shapes, stats=False)
        results.append(r)
    json.dump(results, open(OUT + "/shadow_results.json", "w"), indent=1)
