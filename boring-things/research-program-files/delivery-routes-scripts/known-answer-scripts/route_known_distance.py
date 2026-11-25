"""Delivery route (traveling salesman) search: how much does knowing the best distance shrink the search?

Random cities in a unit square. A "step" is one partial route extended by one city.
Solvers (all return a proven shortest round trip):
  blind      = try every ordering (count from a formula)
  learner    = prune a partial route when partial distance + cheapest possible finish cannot beat the best full route found so far
  told       = same pruning but the true best distance is handed over at the start and the search stops at the first route that matches
  told+10%   = handed a distance 10% above the true best (a rough hint)
The "cheapest possible finish" adds for the current city and every unvisited city the shortest road leaving that city.
"""
import random, math, json, sys
sys.setrecursionlimit(10000)

def solve(D, n, bound0, stop_at=None):
    minout = [min(D[i][j] for j in range(n) if j != i) for i in range(n)]
    order = [sorted((j for j in range(n) if j != i), key=lambda j: D[i][j]) for i in range(n)]
    best = [bound0]; steps = [0]; found = [False]
    visited = [False] * n; visited[0] = True
    def rec(cur, count, length, rest):  # rest = sum of minout over unvisited cities
        if found[0]: return
        if count == n:
            total = length + D[cur][0]
            if total < best[0] - 1e-12 or (stop_at is not None and total <= stop_at + 1e-9):
                best[0] = total
                if stop_at is not None and total <= stop_at + 1e-9: found[0] = True
            return
        for j in order[cur]:
            if visited[j]: continue
            nl = length + D[cur][j]
            if nl + rest > best[0] + 1e-9: continue      # rest includes minout[j] which is the cost of leaving j
            steps[0] += 1
            visited[j] = True
            rec(j, count + 1, nl, rest - minout[j])
            visited[j] = False
            if found[0]: return
    rec(0, 1, 0.0, sum(minout[1:]))
    return best[0], steps[0]

def blind_steps(n):
    return sum(math.factorial(n - 1) // math.factorial(n - 1 - k) for k in range(1, n))

res = []
rng = random.Random(11)
for n, reps in ((7, 30), (8, 30), (9, 30), (10, 30), (11, 20), (12, 10), (13, 6)):
    acc = {"learner": [], "told": [], "told10": []}
    for _ in range(reps):
        P = [(rng.random(), rng.random()) for _ in range(n)]
        D = [[math.dist(a, b) for b in P] for a in P]
        opt, s1 = solve(D, n, float("inf"))
        o2, s2 = solve(D, n, opt, stop_at=opt); assert abs(o2 - opt) < 1e-9
        o3, s3 = solve(D, n, opt * 1.10); assert abs(o3 - opt) < 1e-9
        acc["learner"].append(s1); acc["told"].append(s2); acc["told10"].append(s3)
    gm = lambda v: math.exp(sum(math.log(x) for x in v) / len(v))
    row = {"cities": n, "runs": reps, "blind_steps": blind_steps(n), "learner_steps": round(gm(acc["learner"])),
           "told_plus_10_percent_steps": round(gm(acc["told10"])), "told_steps": round(gm(acc["told"])), "check_steps": n}
    row["learner_over_told"] = round(row["learner_steps"] / row["told_steps"], 2)
    res.append(row); print(row, flush=True)
# growth per added city (ratio of steps from one size to the next, averaged)
def growth(key):
    v = [r[key] for r in res]; return round((v[-1] / v[0]) ** (1 / (len(v) - 1)), 2)
summary = {k: growth(k) for k in ("blind_steps", "learner_steps", "told_plus_10_percent_steps", "told_steps")}
print(summary)
json.dump({"rows": res, "growth_per_added_city": summary}, open("route_known_distance_results.json", "w"), indent=1)
