"""The maze test: three scores for a door grid built from the digits of a prime.

  top-to-bottom crossings = separate regions that join the top row to the bottom row
  side-to-side crossings  = separate regions that join the left column to the right column
  longest                 = the most rooms any walk can visit without entering a room twice
  maze score              = longest + (rooms along one side) x (top-to-bottom crossings + side-to-side crossings)
                            so each crossing is worth one full row of rooms
Also: big grids fed by different prime sources and primes built to make one hallway through every room.
"""
from grid_tools import *
out = {}
# ---- 2 by 2: every 4 digit prime ----
rows = []
for p in range(1000, 10000):
    if gmpy2.is_prime(p):
        adj = build(digits_to_dirs(str(p)), 2); tb, lr = crossings(adj, 2); rows.append((p, tb, lr, longest_walk(adj)))
out["grid2"] = {"primes": len(rows),
    "top_bottom_counts": {str(v): sum(r[1] == v for r in rows) for v in range(3)},
    "side_side_counts": {str(v): sum(r[2] == v for r in rows) for v in range(3)},
    "two_top_bottom_crossings_first_15": [r[0] for r in rows if r[1] == 2][:15], "two_top_bottom_total": sum(r[1] == 2 for r in rows),
    "two_side_side_crossings": [r[0] for r in rows if r[2] == 2][:15],
    "crossing_both_ways": sum(r[1] >= 1 and r[2] >= 1 for r in rows)}
sc2 = sorted(((r[3] + 2 * (r[1] + r[2]), r[0], r[1], r[2], r[3]) for r in rows), key=lambda t: (-t[0], t[1]))
out["grid2"]["score_counts"] = {str(v): sum(t[0] == v for t in sc2) for v in sorted({t[0] for t in sc2}, reverse=True)}
out["grid2"]["top_scores_first_25"] = [{"prime": t[1], "score": t[0], "top_bottom": t[2], "side_side": t[3], "longest": t[4]} for t in sc2[:25]]
# ---- 3 by 3: table of every door pattern then every 9 digit prime ----
T_tb = np.zeros(4 ** 9, dtype=np.int8); T_lr = np.zeros(4 ** 9, dtype=np.int8); T_long = np.zeros(4 ** 9, dtype=np.int8)
for code in range(4 ** 9):
    adj = build([(code >> (2 * i)) & 3 for i in range(9)], 3); T_tb[code], T_lr[code] = crossings(adj, 3); T_long[code] = longest_walk(adj)
lim = 10 ** 9; half = lim // 2
sv = np.ones(half, dtype=bool); sv[0] = False
for i in range(1, int(lim ** 0.5) // 2 + 1):
    if sv[i]:
        p = 2 * i + 1; sv[(p * p) // 2::p] = False
T_score = T_long.astype(np.int64) + 3 * (T_tb.astype(np.int64) + T_lr.astype(np.int64))
counts = np.zeros(4 ** 9, dtype=np.int64); total = 0; ex = {"tb3": [], "both": [], "best": []}; score_ex = {}
CH = 25_000_000
for a in range((10 ** 8) // 2, half, CH):
    idx = np.nonzero(sv[a:min(a + CH, half)])[0].astype(np.int64) + a
    pr = 2 * idx + 1; total += len(pr); code = np.zeros(len(pr), dtype=np.int64); q = pr.copy()
    for pos in range(8, -1, -1):
        d = q % 10; q //= 10; code |= ((d - 1) % 4) << (2 * pos)
    counts += np.bincount(code, minlength=4 ** 9)
    sc = T_score[code]
    for v in np.unique(sc)[-8:].tolist():
        if len(score_ex.setdefault(v, [])) < 8:
            sel = np.nonzero(sc == v)[0][:8 - len(score_ex[v])]
            score_ex[v] += [{"prime": int(pr[i]), "top_bottom": int(T_tb[code[i]]), "side_side": int(T_lr[code[i]]), "longest": int(T_long[code[i]])} for i in sel]
    for key, mask in (("tb3", T_tb[code] == 3), ("both", (T_tb[code] >= 1) & (T_lr[code] >= 1) & (T_long[code] == 9))):
        if len(ex[key]) < 12: ex[key] += pr[mask][:12 - len(ex[key])].tolist()
del sv
out["grid3"] = {"primes": int(total),
    "top_bottom_counts": {str(v): int(counts[T_tb == v].sum()) for v in range(4)},
    "side_side_counts": {str(v): int(counts[T_lr == v].sum()) for v in range(4)},
    "crossing_both_ways": int(counts[(T_tb >= 1) & (T_lr >= 1)].sum()),
    "three_top_bottom_examples": ex["tb3"], "tube_that_crosses_both_ways_examples": ex["both"],
    "tube_that_crosses_both_ways_count": int(counts[(T_tb >= 1) & (T_lr >= 1) & (T_long == 9)].sum())}
vals = sorted({int(v) for v in np.unique(T_score[counts > 0])}, reverse=True)
out["grid3"]["score_counts"] = {str(v): int(counts[T_score == v].sum()) for v in vals}
out["grid3"]["examples_for_top_scores"] = {str(v): score_ex.get(v, [])[:8] for v in vals[:6]}
print(json.dumps(out["grid3"]["score_counts"]), json.dumps(out["grid3"]["examples_for_top_scores"])[:1500], flush=True)
# ---- larger grids: samples of primes ----
rng = random.Random(9); rows = []
for k, reps in ((4, 20000), (5, 20000), (6, 8000), (8, 3000), (10, 2000), (20, 300)):
    tbs = lrs = 0; anytb = anylr = 0; best = (0, None); top = []
    for _ in range(reps):
        s = str(random_prime(k * k, rng)); adj = build(digits_to_dirs(s), k); tb, lr = crossings(adj, k)
        tbs += tb; lrs += lr; anytb += tb > 0; anylr += lr > 0
        if tb + lr > best[0]: best = (tb + lr, s)
        if tb + lr > 0 or k <= 6:
            L = longest_walk(adj); top.append((L + k * (tb + lr), s, tb, lr, L)); top = sorted(top, key=lambda t: -t[0])[:10]
    rows.append({"grid": k, "samples": reps, "average_top_bottom": tbs / reps, "average_side_side": lrs / reps,
                 "share_with_a_top_bottom_crossing": anytb / reps, "share_with_a_side_side_crossing": anylr / reps, "best_total": best[0], "best_prime": best[1],
                 "top_10_by_maze_score": [{"prime": t[1], "score": t[0], "top_bottom": t[2], "side_side": t[3], "longest": t[4]} for t in top]})
    print({a: b for a, b in rows[-1].items() if a != "top_10_by_maze_score"}, [ (t["score"], t["top_bottom"], t["side_side"], t["longest"]) for t in rows[-1]["top_10_by_maze_score"][:4]], flush=True)
out["larger_grids"] = rows
# ---- one big grid (300 by 300 rooms) fed by different sources ----
def small_primes(count):
    n = 2_500_000; s = np.ones(n, dtype=bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0][:count]
K = 300; need = K * K; P = small_primes(need + 3).tolist(); r2 = random.Random(3)
stream = "".join(str(p) for p in P)[:need]
sources = {
 "digits of the primes written in one row": [dir_of(int(ch)) for ch in stream],
 "one whole prime in each room": [dir_of(p) for p in P[:need]],
 "last digit of each prime": [dir_of(p % 10) for p in P[:need]],
 "first digit of each prime": [dir_of(int(str(p)[0])) for p in P[:need]],
 "gap between neighboring primes": [dir_of(P[i + 1] - P[i]) for i in range(need)],
 "half of the gap between neighboring primes": [dir_of((P[i + 2] - P[i + 1]) // 2) for i in range(need)],
 "random digits": [dir_of(r2.randrange(10)) for _ in range(need)],
}
big = []
for name, dirs in sources.items():
    adj = build(dirs, K); comp, sizes = regions(adj); tb, lr = crossings(adj, K)
    walls = sum(len(a) for a in adj) // 2
    share = [round(dirs.count(d) / need, 3) for d in range(4)]
    big.append({"source": name, "door_shares_north_east_south_west": share, "share_of_inner_walls_open": round(walls / (2 * K * (K - 1)), 3),
                "regions": len(sizes), "largest_region": max(sizes), "top_bottom_crossings": tb, "side_side_crossings": lr, "longest": longest_walk(adj)})
    print(big[-1], flush=True)
out["big_grid_300"] = big
# ---- two digits in each room (two doors) : does the grid become one crossable maze? ----
two = []
for name, seq in (("digits of the primes written in one row", "".join(str(p) for p in P)), ("random digits", "".join(str(r2.randrange(10)) for _ in range(3 * need)))):
    for per in (1, 2, 3):
        adj = [set() for _ in range(need)]
        for i in range(need):
            for t in range(per):
                d = dir_of(int(seq[i * per + t])); r, c = divmod(i, K); a, b = r + DR[d][0], c + DR[d][1]
                if 0 <= a < K and 0 <= b < K: adj[i].add(a * K + b); adj[a * K + b].add(i)
        comp, sizes = regions(adj); tb, lr = crossings(adj, K); walls = sum(len(a) for a in adj) // 2
        two.append({"source": name, "digits_in_each_room": per, "share_of_inner_walls_open": round(walls / (2 * K * (K - 1)), 3), "regions": len(sizes),
                    "largest_region_share": round(max(sizes) / need, 3), "corner_to_corner": comp[0] == comp[-1], "top_bottom_crossings": tb, "side_side_crossings": lr})
        print(two[-1], flush=True)
out["more_digits_in_each_room"] = two
# ---- primes built to make one hallway through every room ----
def tube_prime(k, rng):
    path = []
    for r in range(k):
        cs = range(k) if r % 2 == 0 else range(k - 1, -1, -1)
        path += [r * k + c for c in cs]
    br = k * k - 1; ib = path.index(br); want = {}
    def toward(a, b):
        ra, ca = divmod(a, k); rb, cb = divmod(b, k); return DR.index((rb - ra, cb - ca))
    for i, room in enumerate(path):
        if i < ib: want[room] = toward(room, path[i + 1])
        elif i > ib: want[room] = toward(room, path[i - 1])
    opts = {0: "159", 1: "26", 2: "37", 3: "480"}
    for _ in range(200000):
        ds = []
        for room in range(k * k):
            if room == br: ds.append(rng.choice("1379"))
            else:
                ch = rng.choice(opts[want[room]])
                while room == 0 and ch == "0": ch = rng.choice(opts[want[room]])
                ds.append(ch)
        s = "".join(ds)
        if gmpy2.is_prime(int(s), 30): return s
tubes = {}
r3 = random.Random(21)
for k in (4, 5, 6, 8, 10):
    s = tube_prime(k, r3); m = measure(digits_to_dirs(s), k); assert m["longest"] == k * k
    tb, lr = crossings(build(digits_to_dirs(s), k), k); tubes[str(k)] = {"prime": s, "longest": k * k, "top_bottom": tb, "side_side": lr, "score": k * k + k * (tb + lr)}
out["built_tube_primes"] = tubes; print(tubes)
json.dump(out, open("maze_test_results.json", "w"), indent=1)
