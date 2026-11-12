# Reproduces the "cannot set the y limit" problem from matplotlib forum topic 26073 and shows the fix
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
values_from_file = ["1200\n", "9800\n", "4100\n", "13000\n"]   # readline() returns text like this

def run(convert, where):
    fig, ax = plt.subplots()
    xs, ys = [], []
    for i, raw in enumerate(values_from_file):
        ys.append(float(raw) if convert else raw)
        xs.append(i)
        if where == "before_clear":
            ax.set_ylim(0, 15000)
        ax.clear()
        ax.plot(xs, ys)
        if where == "after_plot":
            ax.set_ylim(0, 15000)
    fig.canvas.draw()
    labels = [t.get_text() for t in ax.get_yticklabels()][:4]
    plt.close(fig)
    return ax.get_ylim(), labels

for convert in (False, True):
    for where in ("before_clear", "after_plot"):
        lim, labels = run(convert, where)
        print(f"numbers converted with float(): {convert} | set_ylim placed {where} | y limits {lim} | first tick labels {labels}")
