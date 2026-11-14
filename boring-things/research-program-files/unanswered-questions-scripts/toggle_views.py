# Tests clearing one matplotlib figure and redrawing a different layout in the same window (forum topic 26086)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
rng = np.random.default_rng(0)
fig = plt.figure()
window = fig.canvas.manager          # the object that owns the window
state = {"view": "grid"}

def draw_grid():
    fig.clf()
    axes = fig.subplots(2, 2)
    for ax in axes.flat:
        ax.plot(rng.random(20))

def draw_scatter():
    fig.clf()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(rng.random(50), rng.random(50))

def redraw():
    draw_grid() if state["view"] == "grid" else draw_scatter()
    fig.canvas.draw_idle()

def on_key(event):                    # pressing the t key switches the view
    if event.key == "t":
        state["view"] = "scatter" if state["view"] == "grid" else "grid"
        redraw()

fig.canvas.mpl_connect("key_press_event", on_key)
timer = fig.canvas.new_timer(interval=1000)   # redraw with fresh data once per second
timer.add_callback(redraw)

for step in range(4):
    redraw(); fig.canvas.draw()
    print("view", state["view"], "| number of charts in the figure:", len(fig.axes), "| same figure number:", fig.number == 1, "| same window object:", fig.canvas.manager is window, "| open figures:", len(plt.get_fignums()))
    from matplotlib.backend_bases import KeyEvent
    fig.canvas.callbacks.process("key_press_event", KeyEvent("key_press_event", fig.canvas, "t"))
