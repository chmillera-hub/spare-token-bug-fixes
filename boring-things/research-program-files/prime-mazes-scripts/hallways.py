"""Hallway walks: each number is the length of a hallway and the walker turns right after every hallway.

The walker starts facing north. A hallway may cross an earlier hallway. Scores after all hallways are drawn:
  end distance   = straight-line distance from the start to the end
  box            = width and height of the area the walk covers
  crossing spots = grid points the walk stands on more than once
  repeat share   = share of the steps that landed on a point already visited
"""
import json, random, math
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0].tolist()
P = primes_upto(200000)
digits = [int(c) for c in "".join(map(str, P))]
r = random.Random(4)
N = 2000
sources = {
 "1 2 3 4 5 6 7 8 9 repeated": [(i % 9) + 1 for i in range(N)],
 "1 3 1 3 repeated": [1 if i % 2 == 0 else 3 for i in range(N)],
 "digits of the primes written in one row": digits[:N],
 "last digit of each prime": [p % 10 for p in P[:N]],
 "gap between neighboring primes": [P[i + 1] - P[i] for i in range(N)],
 "the primes themselves": P[:300],
 "random digits": [r.randrange(10) for _ in range(N)],
 "random digits 1 to 9": [r.randrange(1, 10) for _ in range(N)],
}
D = ((0, 1), (1, 0), (0, -1), (-1, 0))
res = []; paths = {}
for name, seq in sources.items():
    x = y = 0; pts = [(0, 0)]; seen = {(0, 0): 1}; steps = repeat = 0
    for i, L in enumerate(seq):
        dx, dy = D[i % 4]
        for _ in range(L):
            x += dx; y += dy; steps += 1
            if (x, y) in seen: repeat += 1
            seen[(x, y)] = seen.get((x, y), 0) + 1
        pts.append((x, y))
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    res.append({"source": name, "hallways": len(seq), "steps": steps, "end_distance": round(math.hypot(x, y), 1),
                "box_width": max(xs) - min(xs), "box_height": max(ys) - min(ys),
                "crossing_spots": sum(1 for v in seen.values() if v > 1), "repeat_share": round(repeat / max(steps, 1), 3),
                "end_point_east_north": [x, y]})
    paths[name] = pts; print(res[-1])
# drift of the digits-of-primes walk against 200 random digit walks of the same length
ends = []
for t in range(200):
    x = y = 0
    for i in range(N):
        L = r.randrange(10); dx, dy = D[i % 4]; x += dx * L; y += dy * L
    ends.append(math.hypot(x, y))
res.append({"random_digit_walks": 200, "average_end_distance": round(sum(ends) / 200, 1), "largest_end_distance": round(max(ends), 1)})
print(res[-1])
json.dump(res, open("hallways_results.json", "w"), indent=1)
fig, axs = plt.subplots(2, 4, figsize=(16, 8.4))
for ax, (name, pts) in zip(axs.flat, paths.items()):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs, ys, lw=0.6, color="#1f4e79"); ax.plot(0, 0, "o", color="#2e8b57", ms=5); ax.plot(xs[-1], ys[-1], "s", color="#c0392b", ms=5)
    ax.set_title(name, fontsize=10); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
fig.suptitle("Hallway walks: each number is a hallway length and the walker turns right after each hallway (green dot = start and red square = end)", fontsize=11)
fig.tight_layout(); fig.savefig("hallway-walks.png", dpi=110)
