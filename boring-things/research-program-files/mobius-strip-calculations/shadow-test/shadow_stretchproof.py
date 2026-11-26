"""Stretch-proof shadow count.

Before two shadows are compared each shadow is stretched and sheared until the
shadow is equally spread in every direction.  Two shadows that are stretched
copies of each other therefore count as one shadow.  Every shadow of a flat
circle becomes the same circle and every shadow of a flat square becomes the
same square under the rule so the rule removes the variety that stretching
alone can make.

Run:  python3 shadow_stretchproof.py [output_folder]
"""
import json
import sys
import numpy as np
from shadow_variety import (BIG, EPS, N_DIR, cube, directions, disk, farthest_first, count_at,
                            loop, mobius, project, raster, rock, shadow_P, sphere, square)

OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def even_spread(P, F, rounds=4):
    Q = P.copy()
    for _ in range(rounds):
        c0 = (Q.max(0) + Q.min(0)) / 2
        s0 = np.linalg.norm(Q - c0, axis=1).max() + 1e-9
        big = raster(Q, F, BIG, c0, s0)
        ys, xs = np.nonzero(big)
        pix = np.c_[xs, ys].astype(float)
        k = s0 / (BIG / 2 * 0.92)
        cen = c0 + (pix.mean(0) - BIG / 2) * k
        w, vec = np.linalg.eigh(np.cov((pix - pix.mean(0)).T) * k * k)
        w = np.maximum(w, 1e-12)
        W = vec @ np.diag(w ** -0.5) @ vec.T
        Q = (Q - cen) @ W.T
    return Q


if __name__ == "__main__":
    out, gallery = [], {}
    D = directions(N_DIR)
    for name, (V, F) in [("sphere", sphere()), ("flat circle", disk()), ("flat square", square()),
                         ("cube", cube()), ("lumpy rock", rock()), ("untwisted loop", loop()),
                         ("Mobius strip", mobius())]:
        imgs = np.array([shadow_P(even_spread(project(V, d), F), F) for d in D])
        picks, gaps = farthest_first(imgs, min(EPS))
        r = {"name": name, "shadows_cast": len(imgs),
             "different_shadows_after_stretching_is_removed": {str(e): count_at(gaps, e) for e in EPS}}
        print(json.dumps(r), flush=True)
        out.append(r)
        gallery[name] = [imgs[p] for p in picks[:10]]
    np.save(OUT + "/gallery_stretchproof.npy", gallery, allow_pickle=True)
    json.dump(out, open(OUT + "/stretchproof_results.json", "w"), indent=1)
