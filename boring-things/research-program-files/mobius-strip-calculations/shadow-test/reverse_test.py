"""Reverse test: can the pose of a Mobius strip be read back from the lit patch
that passes through the middle of the strip or from the whole shadow?

For every light direction the program stores the lit patch and the whole shadow
at true size.  For each stored picture the program then finds every other light
direction whose picture is the same within a small miss and reports how far
apart those look-alike directions are.  The strip looks the same after a half
turn around one line through the strip so two directions related by that half
turn count as the same pose.

Run:  python3 reverse_test.py [output_folder]
"""
import json
import sys
import numpy as np
from scipy import ndimage
from shadow_variety import directions, mobius, project, raster
from hole_light import patch

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
N = 1200
BIG = 200
SCALE = 1.5
SMALL = 64
K = SCALE / (BIG / 2 * 0.92)          # world units per big pixel


def aligned(mask, half_width_world):
    """Centre the picture on the middle of the dark or lit area and turn the long
    axis level.  The size is kept true."""
    ys, xs = np.nonzero(mask)
    pix = np.c_[xs, ys].astype(float)
    cen = pix.mean(0)
    w, vec = np.linalg.eigh(np.cov((pix - cen).T))
    a = np.arctan2(vec[1, 1], vec[0, 1])
    g = (np.arange(SMALL) - SMALL / 2 + 0.5) / (SMALL / 2) * (half_width_world / K)
    U, Vv = np.meshgrid(g, g)
    X = cen[0] + np.cos(a) * U - np.sin(a) * Vv
    Y = cen[1] + np.sin(a) * U + np.cos(a) * Vv
    return ndimage.map_coordinates(mask.astype(np.float32), [Y, X], order=1, cval=0) > 0.5


def turned_copies(img):
    out = []
    for a in np.arange(0, 360, 15):
        if a % 90 == 0:
            r = np.rot90(img, int(a // 90))
        else:
            r = ndimage.rotate(img.astype(np.float32), a, reshape=False, order=1) > 0.5
        out.append(r.ravel())
    return np.array(out, dtype=np.float32)


def look_alikes(imgs, D, tol):
    """For each picture: the largest angle to any light direction whose picture
    is the same within tol (after allowing the half-turn sameness of the strip)."""
    X = imgs.reshape(len(imgs), -1).astype(np.float32)
    areas = X.sum(1)
    half_turn = D * np.array([1, -1, -1])
    worst = []
    for i in range(len(imgs)):
        T = turned_copies(imgs[i])
        inter = X @ T.T
        union = areas[:, None] + T.sum(1)[None, :] - inter
        dist = 1 - (inter / np.maximum(union, 1)).max(1)
        same = np.nonzero(dist <= tol)[0]
        c1 = np.clip(D[same] @ D[i], -1, 1)
        c2 = np.clip(half_turn[same] @ D[i], -1, 1)
        ang = np.degrees(np.arccos(np.maximum(c1, c2)))
        worst.append(float(ang.max()))
    return np.array(worst)


def summary(worst):
    return {"pictures": int(len(worst)),
            "middle_uncertainty_degrees": float(np.median(worst)),
            "share_pinned_within_15_degrees": float((worst <= 15).mean()),
            "share_with_a_look_alike_more_than_30_degrees_away": float((worst > 30).mean())}


if __name__ == "__main__":
    V, F = mobius()
    D = directions(N)
    patches, shadows, has = [], [], []
    for d in D:
        sh = raster(project(V, d), F, BIG, np.zeros(2), SCALE)
        shadows.append(aligned(sh, 1.6))
        m, size = patch(sh)
        if size >= 30:
            patches.append(aligned(m, 0.95))
            has.append(True)
        else:
            has.append(False)
    has = np.array(has)
    res = {"light_directions": N, "share_of_directions_with_a_lit_patch": float(has.mean())}
    for tol in (0.05, 0.10):
        res["lit_patch_alone_miss_%.2f" % tol] = summary(look_alikes(np.array(patches), D[has], tol))
        res["whole_shadow_miss_%.2f" % tol] = summary(look_alikes(np.array(shadows), D, tol))
        print(json.dumps(res), flush=True)

    # mirror check: a left-handed strip turned into the right pose casts the very same shadow
    left = V * np.array([1, 1, -1])
    Hz = np.diag([1.0, 1.0, -1.0])
    worst = 1.0
    for d in D[::100]:
        Hd = np.eye(3) - 2 * np.outer(d, d)
        a = raster(project(V, d), F, BIG, np.zeros(2), SCALE)
        b = raster(project(left @ (Hz @ Hd), d), F, BIG, np.zeros(2), SCALE)
        worst = min(worst, (a & b).sum() / (a | b).sum())
    res["lowest_overlap_between_right_handed_shadow_and_matching_left_handed_shadow"] = float(worst)
    print(json.dumps(res), flush=True)
    json.dump(res, open(OUT + "/reverse_results.json", "w"), indent=1)
