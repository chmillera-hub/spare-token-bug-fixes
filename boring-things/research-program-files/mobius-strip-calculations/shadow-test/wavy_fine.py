"""Stricter count for the fat shapes: two shadows count as different when the
overlap misses by more than 8 parts in 100 (the main test used 25 parts in 100)."""
import json
import numpy as np
from shadow_variety import N_DIR, directions, farthest_first, project, shadow_P, sphere, cube
from wavy import wavy_sphere, wavy_cube
D = directions(N_DIR)
for name, make in [("sphere", sphere), ("wavy sphere", wavy_sphere), ("cube", cube), ("wavy cube", wavy_cube)]:
    V, F = make()
    imgs = np.array([shadow_P(project(V, d), F) for d in D])
    picks, gaps = farthest_first(imgs, 0.08)
    print(json.dumps({"name": name, "different_shadows_at_0.08": len(picks)}), flush=True)
