# Compares a point-by-point polygon lookup with a bulk lookup in shapely 2 on made-up data (Python forum topic 88825)
import time, numpy as np, shapely
from shapely import STRtree, Point
from shapely.geometry import Polygon
print("shapely", shapely.__version__)
rng = np.random.default_rng(0)
def blob(cx, cy):
    ang = np.sort(rng.uniform(0, 2 * np.pi, 40)); rad = rng.uniform(0.3, 1.0, 40)
    return Polygon(np.column_stack([cx + rad * np.cos(ang), cy + rad * np.sin(ang)]))
polys = [blob(*rng.uniform(0, 60, 2)) for _ in range(207)]            # 207 irregular reef-like polygons
n = 200_000
xs, ys = rng.uniform(0, 60, n), rng.uniform(0, 60, n)                  # particle positions for one time step
tree = STRtree(polys)

sample = 20_000
t = time.perf_counter(); slow = np.full(sample, -1)
for i in range(sample):                                               # one Point object and one index lookup per particle
    pt = Point(xs[i], ys[i])
    for j in tree.query(pt):
        if pt.within(polys[j]): slow[i] = j; break
t_slow = (time.perf_counter() - t) / sample * n

t = time.perf_counter()
pts = shapely.points(xs, ys)                                          # all points built in one call
pt_idx, poly_idx = tree.query(pts, predicate="within")               # all lookups in one call
fast = np.full(n, -1); fast[pt_idx[::-1]] = poly_idx[::-1]            # keep the first match per point
t_fast = time.perf_counter() - t
hits = (fast >= 0).sum()
agree = np.array_equal((slow >= 0), (fast[:sample] >= 0))
print(f"{n} particles against 207 polygons | particles inside a polygon: {hits}")
print(f"point-by-point loop (measured on {sample} particles and scaled up): {t_slow:.1f} s | bulk call: {t_fast:.2f} s | speed-up about {t_slow / t_fast:.0f} times")
print("both methods agree on which particles are inside a polygon:", agree)
print(f"scaled to 1,000,000 particles and 720 hourly steps: loop about {t_slow * 5 * 720 / 3600:.1f} hours | bulk about {t_fast * 5 * 720 / 60:.1f} minutes")
