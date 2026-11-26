"""Draws every shadow that counts as different (at the middle setting) for each shape."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shadow_variety import (cube, disk, farthest_first, loop, mobius, shadow, sphere, square, directions, N_DIR)
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
D = directions(N_DIR)
found = {}
for name, (V, F) in [("Sphere", sphere()), ("Cube", cube()), ("Flat circle", disk()),
                     ("Untwisted loop", loop()), ("Flat square", square()), ("Mobius strip", mobius())]:
    imgs = np.array([shadow(V, F, d) for d in D])
    picks, gaps = farthest_first(imgs, 0.25)
    found[name] = [shadow(V, F, D[p], res=96) for p in picks]
    print(name, len(picks), flush=True)

def sheet(names, fname, title, cols=5):
    rows = [(n, -(-len(found[n]) // cols)) for n in names]
    nr = sum(r for _, r in rows)
    fig = plt.figure(figsize=(7.2, 1.62 * nr + 0.5 * len(names) + 0.6), dpi=150)
    fig.suptitle(title, fontsize=14, y=0.997)
    gs = fig.add_gridspec(nr, cols, hspace=0.30, wspace=0.06, top=1 - 0.75 / (1.62 * nr + 0.5 * len(names) + 0.6),
                          bottom=0.01, left=0.02, right=0.98)
    r0 = 0
    for n, r in rows:
        for k, im in enumerate(found[n]):
            ax = fig.add_subplot(gs[r0 + k // cols, k % cols])
            ax.axis("off")
            ax.imshow(~im, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
            if k == 0:
                ax.set_title("%s: %d" % (n, len(found[n])), fontsize=11, loc="left", pad=3)
        r0 += r
    fig.savefig(OUT + "/" + fname, facecolor="white")

sheet(["Mobius strip"], "all-mobius-shadows.png", "All 37 different shadows of the Mobius strip")
sheet(["Sphere", "Cube", "Flat circle", "Untwisted loop", "Flat square"], "all-other-shadows.png",
      "All different shadows of the other shapes")
