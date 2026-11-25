"""How many search steps does knowing the exit save?

Two worlds:
  branching world = a random network where every room has 4 doors (rooms reached grow about 3 times per step)
  flat world      = a square grid maze with 30% of the squares walled off (rooms reached grow like the distance squared)
Solvers:
  blind    = breadth first search from the start that asks "is this the exit?" at every room
  two-end  = knows which room is the exit and searches from both ends until the searches meet
  compass  = (flat world) knows the exit position and always expands the room with the lowest steps-so-far + straight-line steps left
Each solver returns a shortest route. A "step" is one room opened.
"""
import random, json, math, heapq
from collections import deque
import numpy as np

def regular_graph(n, deg, rng):
    # pairing model: random 4 door network (a few double doors or self doors do no harm)
    stubs = np.repeat(np.arange(n), deg); rng.shuffle(stubs)
    adj = [[] for _ in range(n)]
    for a, b in zip(stubs[0::2].tolist(), stubs[1::2].tolist()):
        adj[a].append(b); adj[b].append(a)
    return adj

def blind(adj, s, t):
    seen = {s: 0}; dq = deque([s]); opened = 0
    while dq:
        u = dq.popleft(); opened += 1
        if u == t: return seen[u], opened
        for v in adj(u):
            if v not in seen: seen[v] = seen[u] + 1; dq.append(v)
    return None, opened

def two_end(adj, s, t):
    if s == t: return 0, 1
    da, db = {s: 0}, {t: 0}; fa, fb = [s], [t]; opened = 0; best = None
    while fa and fb:
        if len(fa) <= len(fb): front, mine, other, isa = fa, da, db, True
        else: front, mine, other, isa = fb, db, da, False
        nxt = []
        for u in front:
            opened += 1
            for v in adj(u):
                if v not in mine:
                    mine[v] = mine[u] + 1; nxt.append(v)
                    if v in other:
                        c = mine[v] + other[v]
                        if best is None or c < best: best = c
        if best is not None: return best, opened   # finishing the whole layer keeps the route shortest
        if isa: fa = nxt
        else: fb = nxt
    return None, opened

def branching_world(seed=1):
    rng = np.random.default_rng(seed); r = random.Random(seed)
    n = 3_000_000; g = regular_graph(n, 4, rng); adj = lambda u: g[u]
    rows = {}
    tries = 0
    while tries < 400:
        tries += 1
        s, t = r.randrange(n), r.randrange(n)
        d2, o2 = two_end(adj, s, t)
        if d2 is None: continue
        rows.setdefault(d2, [])
        if len(rows[d2]) >= 25: continue
        d1, o1 = blind(adj, s, t); assert d1 == d2
        rows[d2].append((o1, o2))
    # also plant exits at short chosen distances
    for want in range(3, 11):
        got = rows.setdefault(want, [])
        guard = 0
        while len(got) < 25 and guard < 200:
            guard += 1
            s = r.randrange(n); u = s; path = {s}
            for _ in range(want):
                u = r.choice(g[u])
            d2, o2 = two_end(adj, s, u)
            if d2 != want: continue
            d1, o1 = blind(adj, s, u); got.append((o1, o2))
    out = []
    for d in sorted(rows):
        v = rows[d]
        if len(v) < 8: continue
        a = sum(x[0] for x in v) / len(v); b = sum(x[1] for x in v) / len(v)
        out.append({"distance": d, "runs": len(v), "blind_steps": round(a, 1), "two_end_steps": round(b, 1),
                    "times_fewer": round(a / b, 1), "exponent_ratio": round(math.log(b) / math.log(a), 3)})
    return out

def flat_world(seed=2):
    r = random.Random(seed); N = 1400
    wall = np.array([[r.random() < 0.30 for _ in range(N)] for _ in range(N)])
    def adj(u):
        x, y = u; res = []
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            a, b = x + dx, y + dy
            if 0 <= a < N and 0 <= b < N and not wall[a][b]: res.append((a, b))
        return res
    def compass(s, t):
        h = lambda u: abs(u[0]-t[0]) + abs(u[1]-t[1])
        g = {s: 0}; pq = [(h(s), 0, s)]; opened = 0; done = set()
        while pq:
            f, negg, u = heapq.heappop(pq)
            if u in done: continue
            done.add(u); opened += 1
            if u == t: return g[u], opened
            for v in adj(u):
                if v not in g or g[u] + 1 < g[v]:
                    g[v] = g[u] + 1; heapq.heappush(pq, (g[v] + h(v), -g[v], v))
        return None, opened
    out = []
    for target in (25, 50, 100, 200, 400):
        v = []; guard = 0
        while len(v) < 20 and guard < 4000:
            guard += 1
            sx, sy = r.randrange(450, 950), r.randrange(450, 950)
            ang = r.random() * 2 * math.pi
            tx, ty = int(sx + target * 0.62 * math.cos(ang)), int(sy + target * 0.62 * math.sin(ang))
            if wall[sx][sy] or wall[tx][ty]: continue
            d2, o2 = two_end(adj, (sx, sy), (tx, ty))
            if d2 is None or not (0.8 * target <= d2 <= 1.25 * target): continue
            d1, o1 = blind(adj, (sx, sy), (tx, ty)); d3, o3 = compass((sx, sy), (tx, ty))
            assert d1 == d2 == d3
            v.append((d1, o1, o2, o3))
        m = lambda i: sum(x[i] for x in v) / len(v)
        out.append({"route_length_about": target, "runs": len(v), "average_route_length": round(m(0), 1), "blind_steps": round(m(1)),
                    "two_end_steps": round(m(2)), "compass_steps": round(m(3)),
                    "two_end_times_fewer": round(m(1) / m(2), 2), "compass_times_fewer": round(m(1) / m(3), 2)})
    return out

if __name__ == "__main__":
    res = {"branching_world": branching_world(), "flat_world": flat_world()}
    json.dump(res, open("maze_search_results.json", "w"), indent=1); print(json.dumps(res, indent=1))
