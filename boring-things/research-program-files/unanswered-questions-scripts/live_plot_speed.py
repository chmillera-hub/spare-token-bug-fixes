# Measures drawing strategies for a live line plot with a spectrogram below it (matplotlib forum topic 26255), without a screen
import time, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
fs, seconds = 2000, 4
rng = np.random.default_rng(0)
data = rng.normal(size=fs * seconds)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
(line,) = ax1.plot(np.arange(data.size) / fs, data, lw=0.8, animated=True)
ax1.set_ylim(-6, 6)
spec = np.abs(np.fft.rfft(data.reshape(-1, 200) * np.hanning(200), axis=1)).T
im = ax2.imshow(spec, aspect="auto", origin="lower", animated=True, extent=(0, seconds, 0, fs / 2))
fig.canvas.draw()
background = fig.canvas.copy_from_bbox(fig.bbox)

def timeit(f, n=30):
    t = time.perf_counter()
    for _ in range(n): f()
    return (time.perf_counter() - t) / n * 1000

def draw_line():
    fig.canvas.restore_region(background); ax1.draw_artist(line)
def draw_image():
    fig.canvas.restore_region(background); im.set_data(spec); ax2.draw_artist(im)
def compute_spectrogram():
    np.abs(np.fft.rfft(data.reshape(-1, 200) * np.hanning(200), axis=1))
def full_redraw():
    fig.canvas.draw()

print(f"redrawing only the line with all {data.size} points: {timeit(draw_line):.1f} ms")
print(f"redrawing only the spectrogram image: {timeit(draw_image):.1f} ms")
print(f"computing the spectrogram numbers: {timeit(compute_spectrogram):.2f} ms")

# keeping fast transients while drawing far fewer points: one minimum and one maximum per screen column
def minmax_decimate(y, columns):
    n = (y.size // columns) * columns
    blocks = y[:n].reshape(columns, -1)
    out = np.empty(columns * 2); out[0::2] = blocks.min(axis=1); out[1::2] = blocks.max(axis=1)
    return out
spike = data.copy(); spike[4321] = 25.0                       # a one-sample transient
plain = spike[:: spike.size // 800]
envelope = minmax_decimate(spike, 800)
print("one-sample spike of height 25 | every 10th sample keeps the spike:", plain.max() == 25.0, "| min/max per column keeps the spike:", envelope.max() == 25.0, "| points drawn:", envelope.size, "of", spike.size)
line.set_data(np.linspace(0, seconds, envelope.size), envelope)
print(f"redrawing only the line with {envelope.size} min/max points: {timeit(draw_line):.1f} ms")
