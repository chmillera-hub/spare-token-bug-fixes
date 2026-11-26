"""Draws the five most different shadows of each wavy shape."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
g = np.load(OUT + "/wavy_gallery_plain.npy", allow_pickle=True).item()
counts = {"wavy sphere": (1, 1), "wavy cube": (2, 1), "flat circle with a wavy rim": (9, 12),
          "rippled circle": (9, 17), "wavy untwisted loop": (11, 24), "wavy Mobius strip": (37, 38)}
names = list(counts)
fig = plt.figure(figsize=(7.2, 1.95 * len(names) + 0.8), dpi=150)
fig.suptitle("The most different shadows of each wavy shape", fontsize=15, y=0.995)
gs = fig.add_gridspec(len(names), 5, hspace=0.42, wspace=0.05, top=0.945, bottom=0.01, left=0.02, right=0.98)
for r, n in enumerate(names):
    for k, im in enumerate(g[n][:5]):
        ax = fig.add_subplot(gs[r, k]); ax.axis("off")
        ax.imshow(~im, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
        if k == 0:
            ax.set_title("%s: count went from %d to %d" % (n[0].upper() + n[1:], *counts[n]), fontsize=10.5, loc="left", pad=4)
fig.savefig(OUT + "/wavy-shadow-gallery.png", facecolor="white")
