# Tests a second x axis in degrees Celsius whose ticks sit exactly above the data points of a 1/T plot (forum topic 26117)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
temps_c = np.array([25.0, 50.0, 100.0, 200.0, 400.0])     # made-up measurement temperatures
inv_t = 1.0 / (temps_c + 273.15)                           # x values of the plot (1/K)
values = np.exp(-3000 * inv_t)
fig, ax = plt.subplots()
ax.semilogy(inv_t, values, "o-")
ax.set_xlabel("1/T (1/K)")
with np.errstate(divide="ignore"):
    secax = ax.secondary_xaxis("top", functions=(lambda x: 1.0 / x - 273.15, lambda c: 1.0 / (c + 273.15)))
secax.set_xticks(temps_c)
secax.set_xlabel("temperature (°C)")
fig.canvas.draw()
labels = [t.get_text() for t in secax.get_xticklabels()]
tick_px = [secax.transData.transform((c, 0))[0] for c in temps_c]
data_px = [ax.transData.transform((x, 1))[0] for x in inv_t]
print("top axis labels:", labels)
print("largest sideways gap between a top tick and the data point (pixels):", round(max(abs(a - b) for a, b in zip(tick_px, data_px)), 6))
