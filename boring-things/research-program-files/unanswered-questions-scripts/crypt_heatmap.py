# Draws one value per cell position as colour on a U-shaped crypt outline, mirrored left and right (matplotlib forum topic 26080)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
print("matplotlib", matplotlib.__version__)
n_pos = 20
index = np.array([0.5, 1, 2, 9, 14, 8, 4, 3, 2, 1.5, 1, 1, 0.8, 0.5, 0.5, 0.3, 0.2, 0.2, 0.1, 0.1])   # made-up apoptotic index (%) for positions 1 to 20

def centre_line(s, R=1.0, straight=6.0):
    # point and outward direction at distance s along a half crypt: a quarter circle at the bottom, then a straight wall going up
    arc = np.pi * R / 2
    if s <= arc:
        ang = s / R                      # 0 at the very bottom
        return np.array([R * np.sin(ang), -R * np.cos(ang)]), np.array([np.sin(ang), -np.cos(ang)])
    return np.array([R, s - arc]), np.array([1.0, 0.0])

total = np.pi / 2 + 6.0
edges = np.linspace(0, total, n_pos + 1)
thick = 0.45
patches, values = [], []
for k in range(n_pos):
    ss = np.linspace(edges[k], edges[k + 1], 8)
    inner = [centre_line(s)[0] for s in ss]
    outer = [centre_line(s)[0] + thick * centre_line(s)[1] for s in ss]
    cell = np.array(inner + outer[::-1])
    for mirror in (1, -1):               # right half and mirrored left half
        patches.append(Polygon(cell * [mirror, 1], closed=True)); values.append(index[k])
fig, ax = plt.subplots(figsize=(3.2, 6))
coll = PatchCollection(patches, cmap="Reds", edgecolor="black", linewidth=0.8)
coll.set_array(np.array(values)); coll.set_clim(0, index.max())
ax.add_collection(coll)
for k in (0, 4, 9, 14, 19):
    p, d = centre_line((edges[k] + edges[k + 1]) / 2)
    ax.text(*(p + (thick + 0.25) * d), str(k + 1), ha="center", va="center", fontsize=8)
ax.set_aspect("equal"); ax.autoscale_view(); ax.margins(0.1); ax.axis("off")
fig.colorbar(coll, ax=ax, label="apoptotic index (%)", shrink=0.6)
fig.savefig("crypt.png", dpi=110, bbox_inches="tight")
print("cells drawn:", len(patches), "| darkest cell is position", int(np.argmax(index)) + 1, "| colour scale", coll.get_clim())
rgba = coll.to_rgba(np.array(values))
print("position 5 is drawn darker than position 1:", rgba[2 * 4][:3].sum() < rgba[0][:3].sum(), "| left and right copies share the same colour:", all((rgba[2 * k] == rgba[2 * k + 1]).all() for k in range(n_pos)))
