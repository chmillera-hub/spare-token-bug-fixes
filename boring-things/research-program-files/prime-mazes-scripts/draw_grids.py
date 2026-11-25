"""Draw door grids: six sources on a 40 by 40 grid and a sheet of champion primes."""
from grid_tools import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def draw(ax, adj, k, title, digits=None, color_regions=True):
    comp, sizes = regions(adj)
    if color_regions:
        order = sorted(range(len(sizes)), key=lambda i: -sizes[i]); pal = ["#f4b942", "#7fc8f8", "#9bdeac", "#f7a8b8", "#c9b6e4"]
        col = {order[i]: pal[i] for i in range(min(5, len(order))) if sizes[order[i]] >= max(4, k // 4)}
        for i in range(k * k):
            if comp[i] in col:
                r, c = divmod(i, k); ax.add_patch(plt.Rectangle((c, k - 1 - r), 1, 1, color=col[comp[i]], lw=0))
    lw = 1.6 if k <= 10 else 0.7
    for i in range(k * k):
        r, c = divmod(i, k); x, y = c, k - 1 - r
        if c + 1 < k and (i + 1) not in adj[i]: ax.plot([x + 1, x + 1], [y, y + 1], color="k", lw=lw)
        if r + 1 < k and (i + k) not in adj[i]: ax.plot([x, x + 1], [y, y], color="k", lw=lw)
        if digits: ax.text(x + .5, y + .5, digits[i], ha="center", va="center", fontsize=max(6, 16 - k), color="#333")
    ax.add_patch(plt.Rectangle((0, 0), k, k, fill=False, lw=2)); ax.set_xlim(-.2, k + .2); ax.set_ylim(-.2, k + .2)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title, fontsize=10)

def small_primes(count):
    n = 400000; s = np.ones(n, dtype=bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0][:count].tolist()
K = 40; need = K * K; P = small_primes(2 * need + 3); r2 = random.Random(3); stream = "".join(map(str, P))
def two_door(seq):
    adj = [set() for _ in range(need)]
    for i in range(need):
        for t in range(2):
            d = dir_of(int(seq[2 * i + t])); r, c = divmod(i, K); a, b = r + DR[d][0], c + DR[d][1]
            if 0 <= a < K and 0 <= b < K: adj[i].add(a * K + b); adj[a * K + b].add(i)
    return adj
panels = [
 ("digits of the primes written in one row", build([dir_of(int(c)) for c in stream[:need]], K)),
 ("one whole prime in each room (hallways run north and south)", build([dir_of(p) for p in P[:need]], K)),
 ("gap between neighboring primes (hallways run east and west)", build([dir_of(P[i + 1] - P[i]) for i in range(need)], K)),
 ("first digit of each prime (bands)", build([dir_of(int(str(p)[0])) for p in P[:need]], K)),
 ("random digits", build([dir_of(r2.randrange(10)) for _ in range(need)], K)),
 ("digits of the primes with two digits in each room", two_door(stream)),
]
fig, axs = plt.subplots(2, 3, figsize=(16.5, 11.4))
for ax, (t, adj) in zip(axs.flat, panels): draw(ax, adj, K, t)
fig.suptitle("Door grids of 40 by 40 rooms: each room reads a number and opens one door (1 north and 2 east and 3 south and 4 west and then the cycle repeats). The five largest regions are colored.", fontsize=11)
fig.tight_layout(h_pad=3.0); fig.savefig("door-grids.png", dpi=95)

res = json.load(open("maze_test_results.json"))
champs = [("1019 (one hallway through all 4 rooms)", "1019", 2), ("3119 (two top-to-bottom crossings)", "3119", 2),
          ("100101299 (smallest 9 digit prime that makes one hallway through all 9 rooms)", "100101299", 3),
          ("111111199 (three top-to-bottom crossings)", "111111199", 3),
          ("a 16 digit prime built to make one hallway", res["built_tube_primes"]["4"]["prime"], 4),
          ("a 25 digit prime built to make one hallway", res["built_tube_primes"]["5"]["prime"], 5),
          ("best of 20000 random 16 digit primes", res["larger_grids"][0]["top_10_by_maze_score"][0]["prime"], 4),
          ("best of 20000 random 25 digit primes", res["larger_grids"][1]["top_10_by_maze_score"][0]["prime"], 5)]
fig, axs = plt.subplots(2, 4, figsize=(16.5, 8.8))
for ax, (t, s, k) in zip(axs.flat, champs):
    import textwrap
    draw(ax, build(digits_to_dirs(s), k), k, "\n".join(textwrap.wrap(t, 38)), digits=list(s))
fig.suptitle("Primes on door grids: the digits fill the rooms row by row and each digit opens one door", fontsize=12)
fig.tight_layout(); fig.savefig("champion-primes.png", dpi=95)
print(champs[-2][1], champs[-1][1])
