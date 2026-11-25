"""Write the ranking list of primes by maze score and compare 9 digit primes with all 9 digit numbers on the crossings."""
from grid_tools import *
res = json.load(open("maze_test_results.json")); dg = json.load(open("door_grid_results.json"))
L = []
A = L.append
A("Ranking list for the maze test (door grids made from the digits of primes)")
A("")
A("Maze score = longest walk + (rooms along one side) x (top-to-bottom crossings + side-to-side crossings).")
A("Each line: prime then score then top-to-bottom crossings then side-to-side crossings then longest walk.")
A("")
A("GRID OF 2 BY 2 ROOMS: every 4 digit prime (1061 primes) ranked by maze score. The highest possible score is 8.")
rows = []
for p in range(1000, 10000):
    if gmpy2.is_prime(p):
        adj = build(digits_to_dirs(str(p)), 2); tb, lr = crossings(adj, 2); lw = longest_walk(adj); rows.append((lw + 2 * (tb + lr), p, tb, lr, lw))
rows.sort(key=lambda t: (-t[0], t[1]))
for t in rows: A("%d  score %d  top-bottom %d  side-side %d  longest %d" % (t[1], t[0], t[2], t[3], t[4]))
A("")
A("GRID OF 3 BY 3 ROOMS: counts for all 45086079 primes with 9 digits. The highest score any 9 digit prime reached is 15.")
for v, c in res["grid3"]["score_counts"].items(): A("score %s: %d primes" % (v, c))
A("")
A("The first primes found for each of the six highest scores:")
for v, ex in res["grid3"]["examples_for_top_scores"].items():
    for e in ex: A("%d  score %s  top-bottom %d  side-side %d  longest %d" % (e["prime"], v, e["top_bottom"], e["side_side"], e["longest"]))
A("")
A("The first 9 digit primes with three top-to-bottom crossings (score 12): " + " ".join(map(str, res["grid3"]["three_top_bottom_examples"])))
A("")
for row in res["larger_grids"]:
    if not row["top_10_by_maze_score"]: continue
    k = row["grid"]
    A("GRID OF %d BY %d ROOMS: the ten highest scores among %d random primes with %d digits. A single hallway through every room would score %d." % (k, k, row["samples"], k * k, k * k + 2 * k))
    for t in row["top_10_by_maze_score"]: A("%s  score %d  top-bottom %d  side-side %d  longest %d" % (t["prime"], t["score"], t["top_bottom"], t["side_side"], t["longest"]))
    A("")
A("PRIMES BUILT ON PURPOSE to make one hallway through every room (the highest longest walk possible):")
for k, t in res["built_tube_primes"].items(): A("%s by %s rooms: %s  score %d" % (k, k, t["prime"], t["score"]))
open("ranking-list.txt", "w").write("\n".join(L) + "\n")
# all 9 digit numbers against 9 digit primes on crossings
T_tb = np.zeros(4 ** 9, dtype=np.int8); T_lr = np.zeros(4 ** 9, dtype=np.int8)
for code in range(4 ** 9):
    adj = build([(code >> (2 * i)) & 3 for i in range(9)], 3); T_tb[code], T_lr[code] = crossings(adj, 3)
w_first = np.array([3, 2, 2, 2]); w_rest = np.array([3, 2, 2, 3]); codes = np.arange(4 ** 9); wt = w_first[codes & 3].astype(np.float64)
for i in range(1, 9): wt *= w_rest[(codes >> (2 * i)) & 3]
extra = {"all_9_digit_numbers_share_with_top_bottom_crossing": float(wt[T_tb >= 1].sum() / wt.sum()),
         "all_9_digit_numbers_share_with_side_side_crossing": float(wt[T_lr >= 1].sum() / wt.sum()),
         "all_9_digit_numbers_share_crossing_both_ways": float(wt[(T_tb >= 1) & (T_lr >= 1)].sum() / wt.sum())}
json.dump(extra, open("ranking_extra_results.json", "w"), indent=1); print(extra)
print(json.dumps(dg["grid2_all_4_digit_numbers"]), json.dumps(res["grid2"]["score_counts"]), res["grid2"]["top_scores_first_25"][:3])
print(len(L))
