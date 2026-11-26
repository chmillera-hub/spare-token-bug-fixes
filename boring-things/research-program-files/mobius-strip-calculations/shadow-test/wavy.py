"""Shadow counts for wavy versions of the shapes.

Run:  python3 wavy.py plain|proof [output_folder]
  plain = count shadows that differ after free turning and mirror flipping
  proof = same count after every shadow is first stretched to an even spread
          so stretched copies of one shadow count as one shadow
"""
import json
import sys
import numpy as np
from shadow_variety import (N_DIR, directions, farthest_first, grid_mesh, project, shadow_P)
from shadow_stretchproof import even_spread

MODE = sys.argv[1] if len(sys.argv) > 1 else "plain"
OUT = sys.argv[2] if len(sys.argv) > 2 else "."
A = 0.15   # height of the waves compared with a shape of size 1


def wavy_edge_circle():
    """Flat circle whose rim goes in and out six times (still completely flat)."""
    t = np.linspace(0, 2 * np.pi, 145)[:-1]
    r = 1 + A * np.sin(6 * t)
    V = np.vstack([[0, 0, 0], np.c_[r * np.cos(t), r * np.sin(t), 0 * t]])
    F = [(0, 1 + i, 1 + (i + 1) % 144) for i in range(144)]
    return V, np.array(F)


def rippled_circle():
    """Circle rippled up and down three times around like a potato chip."""
    f = lambda t, r: (r * np.cos(t), r * np.sin(t), A * r * np.sin(3 * t))
    return grid_mesh(f, 72, 6, 0, 2 * np.pi, 0, 1)


def wavy_sphere():
    f = lambda u, v: tuple((1 + A * np.sin(3 * u) * np.sin(2 * v)) *
                           np.array([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)]))
    return grid_mesh(f, 48, 24, 0, 2 * np.pi, 0, np.pi)


def wavy_cube():
    """Cube whose six faces each bulge out and in (two waves across each face)."""
    Vs, Fs, off = [], [], 0
    for axis in range(3):
        for sign in (-1, 1):
            def f(a, b, axis=axis, sign=sign):
                p = np.zeros(3)
                p[axis] = sign * (1 + A * np.sin(np.pi * a) * np.sin(np.pi * b))
                p[(axis + 1) % 3] = a
                p[(axis + 2) % 3] = b
                return tuple(p)
            V, F = grid_mesh(f, 12, 12, -1, 1, -1, 1)
            Vs.append(V)
            Fs.append(F + off)
            off += len(V)
    return np.vstack(Vs), np.vstack(Fs)


def _normal_push(base, wave, nu, nv, w):
    """Push every point of a band along the direction that points straight out of the band."""
    h = 1e-4

    def f(u, v):
        p = np.array(base(u, v))
        du = (np.array(base(u + h, v)) - np.array(base(u - h, v))) / (2 * h)
        dv = (np.array(base(u, v + h)) - np.array(base(u, v - h))) / (2 * h)
        n = np.cross(du, dv)
        n /= np.linalg.norm(n)
        return tuple(p + wave(u) * n)
    return grid_mesh(f, nu, nv, 0, 2 * np.pi, -w, w)


def wavy_mobius(w=0.4):
    base = lambda u, v: ((1 + v * np.cos(u / 2)) * np.cos(u),
                         (1 + v * np.cos(u / 2)) * np.sin(u),
                         v * np.sin(u / 2))
    # four and a half waves so the ripples join up smoothly after the half twist
    return _normal_push(base, lambda u: A * np.sin(4.5 * u), 144, 6, w)


def wavy_loop(w=0.4):
    base = lambda u, v: (np.cos(u), np.sin(u), v)
    return _normal_push(base, lambda u: A * np.sin(5 * u), 144, 4, w)


SHAPES = [("wavy sphere", wavy_sphere), ("wavy cube", wavy_cube),
          ("flat circle with a wavy rim", wavy_edge_circle), ("rippled circle", rippled_circle),
          ("wavy untwisted loop", wavy_loop), ("wavy Mobius strip", wavy_mobius)]

if __name__ == "__main__":
    D = directions(N_DIR)
    out, gallery = [], {}
    for name, make in SHAPES:
        V, F = make()
        if MODE == "plain":
            imgs = np.array([shadow_P(project(V, d), F) for d in D])
        else:
            imgs = np.array([shadow_P(even_spread(project(V, d), F), F) for d in D])
        picks, gaps = farthest_first(imgs, 0.25)
        r = {"name": name, "mode": MODE, "different_shadows_at_0.25": len(picks)}
        print(json.dumps(r), flush=True)
        out.append(r)
        gallery[name] = [shadow_P(project(V, D[p]), F, res=96) for p in picks[:10]]
    np.save(OUT + "/wavy_gallery_%s.npy" % MODE, gallery, allow_pickle=True)
    json.dump(out, open(OUT + "/wavy_results_%s.json" % MODE, "w"), indent=1)
