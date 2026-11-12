# Tests bin edges that centre histogram bars on whole numbers (SageMath board question 83318)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
print("matplotlib", matplotlib.__version__)
data = [1,1,1,1,1,1,2,1,1,2,2,2,2,4,4,3,4]
fig, (ax1, ax2) = plt.subplots(1, 2)
counts, edges, bars = ax1.hist(data)
print("default call: 10 bins with edges", np.round(edges, 2).tolist())
print("   bar that holds the value 1 spans", [round(float(bars[0].get_x()), 2), round(float(bars[0].get_x() + bars[0].get_width()), 2)], "| bar that holds the value 4 spans", [round(float(bars[-1].get_x()), 2), round(float(bars[-1].get_x() + bars[-1].get_width()), 2)])
bins = np.arange(min(data) - 0.5, max(data) + 1.5, 1)
counts, edges, bars = ax2.hist(data, bins=bins, rwidth=0.9)
centres = [round(float(b.get_x() + b.get_width() / 2), 6) for b in bars]
print("bins at half numbers:", bins.tolist(), "| bar centres:", centres, "| counts:", counts.astype(int).tolist())
print("every bar is centred on a whole number:", centres == [1.0, 2.0, 3.0, 4.0], "| counts match the data:", counts.astype(int).tolist() == [data.count(v) for v in (1, 2, 3, 4)])
