# Tests two layouts for an image with a row-maximum plot beside it at the same height (matplotlib forum topic 26077)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
print("matplotlib", matplotlib.__version__)
A = np.random.rand(64, 256); B = np.random.rand(64, 128)

def box(fig, ax):
    # final on-screen box of a chart in pixels (charts attached with make_axes_locatable are placed by a locator)
    loc = ax.get_axes_locator()
    if loc is None:
        return ax.get_window_extent()
    return loc(ax, fig.canvas.get_renderer()).transformed(fig.transFigure)

def report(name, fig, pairs):
    fig.canvas.draw()
    for label, (im_ax, side_ax) in zip("AB", pairs):
        a = box(fig, im_ax); b = box(fig, side_ax)
        print(f"{name} | matrix {label}: image {a.width:.0f} by {a.height:.0f} px | side plot height {b.height:.0f} px | tops differ by {abs(a.y1 - b.y1):.2f} px | same y range: {im_ax.get_ylim() == side_ax.get_ylim()}")

# the posted 2 by 2 grid for comparison
fig = plt.figure(); pairs = []
for i, M in enumerate((A, B)):
    ax1 = plt.subplot(2, 2, 2 * i + 1); ax1.imshow(M)
    ax2 = plt.subplot(2, 2, 2 * i + 2); ax2.plot(M.max(axis=1), np.arange(64)); pairs.append((ax1, ax2))
report("posted grid        ", fig, pairs); plt.close(fig)

# layout 1: keep square pixels and attach the side plot to the image
fig, axes = plt.subplots(2, 1); pairs = []
for ax, M in zip(axes, (A, B)):
    ax.imshow(M)
    side = make_axes_locatable(ax).append_axes("right", size=0.8, pad=0.1, sharey=ax)
    side.plot(M.max(axis=1), np.arange(M.shape[0])); side.tick_params(labelleft=False); pairs.append((ax, side))
report("attached side plot ", fig, pairs)
top, bottom = box(fig, pairs[0][0]), box(fig, pairs[1][0])
print("attached side plot  | the two images overlap:", top.y0 < bottom.y1, "| image pixels are square:", pairs[0][0].get_aspect() == 1.0)
plt.close(fig)

# layout 2: a grid with a wide and a narrow column and stretched pixels
fig, axes = plt.subplots(2, 2, width_ratios=[4, 1], sharey="row", layout="constrained"); pairs = []
for (ax, side), M in zip(axes, (A, B)):
    ax.imshow(M, aspect="auto"); side.plot(M.max(axis=1), np.arange(M.shape[0])); pairs.append((ax, side))
report("grid, aspect='auto'", fig, pairs); plt.close(fig)
