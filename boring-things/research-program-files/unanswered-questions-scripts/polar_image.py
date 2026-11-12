# Rebuilds the polar imshow problem from matplotlib forum topic 26078 with a small made-up array and tests a fix
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
orientations = np.linspace(214, 314, 160)          # degrees, one per column
inclinations = np.linspace(-20, 20, 80)            # degrees, one per row
depth = 100 + 2027 * np.random.default_rng(0).random((80, 160))   # metres, largest value about 2127

def new_axes():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(1, 1, 1, projection="polar")
    ax.set_theta_zero_location("N"); ax.set_theta_direction(-1)
    return fig, ax

def coloured_angles(fig, ax):
    # compass angles (degrees clockwise from north) of the pixels that carry image colour
    fig.canvas.draw()
    img = np.asarray(fig.canvas.buffer_rgba())[:, :, :3].astype(int)
    h, w = img.shape[:2]
    x0, y0, x1, y1 = ax.get_window_extent().extents
    cx, cy = (x0 + x1) / 2, h - (y0 + y1) / 2
    ys, xs = np.nonzero((np.abs(img[:, :, 0] - img[:, :, 1]) > 40) | (np.abs(img[:, :, 1] - img[:, :, 2]) > 40))
    ang = (np.degrees(np.arctan2(xs - cx, cy - ys)) + 360) % 360
    return round(float(ang.min())), round(float(ang.max())), len(xs)

# 1. the posted approach
fig, ax = new_axes()
extent = [np.radians(orientations[0]), np.radians(orientations[-1]), depth.min(), depth.max()]
ax.imshow(depth, extent=extent, cmap="viridis")
print("imshow:     angle limits (degrees)", np.round(np.degrees(ax.get_xlim()), 1), "| radius limits", np.round(ax.get_ylim(), 1), "| aspect", ax.get_aspect())
print("imshow:     coloured pixels span compass angles", coloured_angles(fig, ax)[:2])
plt.close(fig)

# 2. pcolormesh with the angle of every column and a radius for every row
fig, ax = new_axes()
theta = np.radians(orientations)
radius = inclinations - inclinations.min()          # 0 at the lowest row
mesh = ax.pcolormesh(theta, radius, depth, cmap="viridis", shading="auto", vmin=depth.min(), vmax=depth.max())
ax.set_rlim(0, radius.max())
span = coloured_angles(fig, ax)[:2]                 # measured before the colour bar is added
fig.colorbar(mesh, ax=ax, label="depth (m)")
print("pcolormesh: angle limits (degrees)", np.round(np.degrees(ax.get_xlim()), 1), "| radius limits", np.round(ax.get_ylim(), 1))
print("pcolormesh: coloured pixels span compass angles", span, "| colour scale", mesh.get_clim())
fig.savefig("polar_fixed.png", dpi=60)
