"""Three part score for a door grid built from the digits of a prime (proposed by the repository author).

  three part score = largest region + longest walk + door points

  largest region = the most rooms joined together by open doors
  longest walk   = the most rooms any walk can visit without entering a room twice
  door points    = 1 point for each spot on the outer wall where a walker could open a door from outside and
                   walk through joined rooms to the opposite side of the grid (a grid of k by k rooms has 4k spots)

Run with MAZE_RULE=zero-north for the version of the rule where 0 opens north.
"""
from grid_tools import *
def door_points(comp, k):
    """One point for each spot on the outer wall where a walker could come in and walk to the opposite side.
    A grid of k by k rooms has 4k spots (k on each side) and a corner room has two spots."""
    top = {comp[c] for c in range(k)}; bot = {comp[(k - 1) * k + c] for c in range(k)}
    left = {comp[r * k] for r in range(k)}; right = {comp[r * k + k - 1] for r in range(k)}
    pts = sum(comp[c] in bot for c in range(k)) + sum(comp[(k - 1) * k + c] in top for c in range(k))
    pts += sum(comp[r * k] in right for r in range(k)) + sum(comp[r * k + k - 1] in left for r in range(k))
    return pts
def parts(dirs, k):
    adj = build(dirs, k); comp, sizes = regions(adj); tb, lr = crossings(adj, k)
    return max(sizes), longest_walk(adj), door_points(comp, k), tb + lr
def score(t): return t[0] + t[1] + t[2]
out = {"rule": "zero-north" if ZERO_NORTH else "one-north"}
# ---- 2 by 2: every 4 digit prime ----
rows = []
for p in range(1000, 10000):
    if gmpy2.is_prime(p):
        t = parts(digits_to_dirs(str(p)), 2); rows.append((score(t), p) + t)
rows.sort(key=lambda r: (-r[0], r[1]))
out["grid2"] = [{"prime": r[1], "score": r[0], "largest_region": r[2], "longest": r[3], "door_points": r[4], "crossings": r[5]} for r in rows]
# ---- 3 by 3: table of every door pattern then every 9 digit prime ----
N = 4 ** 9
T = np.zeros((N, 4), dtype=np.int8)
for code in range(N): T[code] = parts([(code >> (2 * i)) & 3 for i in range(9)], 3)
T_score = T[:, 0].astype(np.int64) + T[:, 1] + T[:, 2]
lim = 10 ** 9; half = lim // 2
sv = np.ones(half, dtype=bool); sv[0] = False
for i in range(1, int(lim ** 0.5) // 2 + 1):
    if sv[i]:
        p = 2 * i + 1; sv[(p * p) // 2::p] = False
counts = np.zeros(N, dtype=np.int64); total = 0; first = {}
CH = 25_000_000
for a in range((10 ** 8) // 2, half, CH):
    idx = np.nonzero(sv[a:min(a + CH, half)])[0].astype(np.int64) + a
    pr = 2 * idx + 1; total += len(pr); code = np.zeros(len(pr), dtype=np.int64); q = pr.copy()
    for pos in range(8, -1, -1):
        d = q % 10; q //= 10; code |= ((d - OFF) % 4) << (2 * pos)
    counts += np.bincount(code, minlength=N); sc = T_score[code]
    for v in np.unique(sc).tolist():
        have = first.setdefault(v, [])
        if len(have) < 40:
            for i in np.nonzero(sc == v)[0][:40 - len(have)]:
                c = int(code[i]); have.append({"prime": int(pr[i]), "score": v, "largest_region": int(T[c, 0]), "longest": int(T[c, 1]), "door_points": int(T[c, 2]), "crossings": int(T[c, 3])})
del sv
vals = sorted({int(v) for v in np.unique(T_score[counts > 0])}, reverse=True)
best_code = int(np.argmax(T_score)); best_pts_code = int(np.argmax(T[:, 2]))
out["grid3"] = {"primes": int(total), "score_counts": {str(v): int(counts[T_score == v].sum()) for v in vals},
                "first_primes_for_each_score": {str(v): first[v] for v in vals},
                "highest_score_any_door_pattern": int(T_score.max()), "most_door_points_any_door_pattern": int(T[:, 2].max()),
                "most_door_points_any_prime": int(T[counts > 0, 2].max()),
                "door_point_counts": {str(v): int(counts[T[:, 2] == v].sum()) for v in range(int(T[:, 2].max()) + 1) if counts[T[:, 2] == v].sum() > 0}}
# ---- 4 by 4 and 5 by 5: samples of random primes (the same primes as maze_test.py) ----
rng = random.Random(9); big = []
for k, reps in ((4, 20000), (5, 20000)):
    top = []; hist = {}
    for _ in range(reps):
        s = str(random_prime(k * k, rng)); t = parts(digits_to_dirs(s), k); v = score(t); hist[v] = hist.get(v, 0) + 1
        top.append((v, s) + t); top = sorted(top, key=lambda r: (-r[0], r[1]))[:25]
    big.append({"grid": k, "samples": reps, "score_counts": {str(v): hist[v] for v in sorted(hist, reverse=True)},
                "top_25": [{"prime": r[1], "score": r[0], "largest_region": r[2], "longest": r[3], "door_points": r[4], "crossings": r[5]} for r in top]})
out["larger_grids"] = big
# ---- primes built to make one hallway ----
res = json.load(open("maze_test_results%s.json" % SUF)); built = {}
for k, t in res["built_tube_primes"].items():
    k = int(k); p = parts(digits_to_dirs(t["prime"]), k)
    built[str(k)] = {"prime": t["prime"], "score": score(p), "largest_region": p[0], "longest": p[1], "door_points": p[2], "crossings": p[3]}
out["built"] = built
out["grid3"]["best_pattern_doors"] = [(best_code >> (2 * i)) & 3 for i in range(9)]; out["grid3"]["most_points_pattern_doors"] = [(best_pts_code >> (2 * i)) & 3 for i in range(9)]
json.dump(out, open("three_part_score_results%s.json" % SUF, "w"), indent=1)
print(out["grid3"]["score_counts"], [ (r["prime"], r["score"]) for r in out["grid2"][:3]], [(b["grid"], b["top_25"][0]) for b in big], built)
