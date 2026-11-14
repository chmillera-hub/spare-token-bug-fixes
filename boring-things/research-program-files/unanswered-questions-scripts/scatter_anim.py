# Rebuilds the scatter animation problem from matplotlib forum topic 26094 and tests the fix
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation
print("matplotlib", matplotlib.__version__)
time_range, n_points = 40, 1000
rng = np.random.default_rng(0)
cord_x = np.cumsum(rng.normal(size=(time_range, n_points)), axis=0)
cord_y = np.cumsum(rng.normal(size=(time_range, n_points)), axis=0)
fig, ax = plt.subplots()
scat = ax.scatter(cord_x[0], cord_y[0])

# the posted update step at frames 0 to 2
for frame in (0, 1, 2):
    data = np.stack([cord_x[:frame], cord_y[:frame]]); data = np.transpose(data, (1, 0, 2))
    try:
        scat.set_offsets(data); fig.canvas.draw()
        print("posted code at frame", frame, "| shape", data.shape, "| no error")
    except Exception as e:
        print("posted code at frame", frame, "| shape", data.shape, "|", type(e).__name__ + ":", e)

# the fix: one row per point and two columns (x and y) taken from a single time step
def update(frame):
    scat.set_offsets(np.column_stack([cord_x[frame], cord_y[frame]]))
    return (scat,)
ax.set_xlim(cord_x.min(), cord_x.max()); ax.set_ylim(cord_y.min(), cord_y.max())
ani = animation.FuncAnimation(fig=fig, func=update, frames=time_range, interval=50)
for frame in (0, 1, time_range - 1):
    update(frame); fig.canvas.draw()
    off = scat.get_offsets()
    print("fixed code at frame", frame, "| offsets shape", off.shape, "| matches the data:", np.allclose(off[:, 0], cord_x[frame]) and np.allclose(off[:, 1], cord_y[frame]))
ani.save("scatter_test.gif", writer="pillow", fps=20)
import os; print("animation file written with", time_range, "frames:", os.path.getsize("scatter_test.gif") > 0)
