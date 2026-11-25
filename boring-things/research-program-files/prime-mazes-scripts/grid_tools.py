"""Door grids from the digits of primes.

Rule (proposed by the repository author): a square grid of rooms. Each room reads one digit and opens one door:
digit 1 -> north, 2 -> east, 3 -> south, 4 -> west, then the cycle repeats (5 north, 6 east, 7 south, 8 west, 9 north, 0 west).
A door opened from either side joins the two rooms. A door that points outside the grid joins nothing.
Digits fill the grid row by row starting at the top left room.

For a grid of k by k rooms a prime with k*k digits fills the grid exactly.
finish  = a walk through open doors exists from the top left room to the bottom right room
longest = the most rooms any walk can visit without entering a room twice
tube    = longest equals the number of rooms (one hallway through every room)
"""
import json, random, math, sys
import numpy as np
import gmpy2
sys.setrecursionlimit(100000)
DR = ((-1, 0), (0, 1), (1, 0), (0, -1))   # north east south west
# Two versions of the rule. Set the environment variable MAZE_RULE=zero-north to use the second version.
#   one-north  (first version):  1 5 9 north; 2 6 east; 3 7 south; 4 8 0 west   -> door = (digit - 1) mod 4
#   zero-north (second version): 0 4 8 north; 1 5 9 east; 2 6 south; 3 7 west   -> door = digit mod 4
import os
ZERO_NORTH = os.environ.get("MAZE_RULE", "one-north") == "zero-north"
OFF = 0 if ZERO_NORTH else 1
SUF = "_zero_north" if ZERO_NORTH else ""          # added to the names of result files
DASH = "-zero-north" if ZERO_NORTH else ""         # added to the names of pictures and lists
def dir_of(d): return (d - OFF) % 4
_ORDER = range(10) if ZERO_NORTH else list(range(1, 10)) + [0]   # the first version lists 0 last so earlier built primes come out the same
OPTS = {k: "".join(str(d) for d in _ORDER if dir_of(d) == k) for k in range(4)}   # digits that open each door
W_REST = [len(OPTS[k]) for k in range(4)]                                            # digits for each door (any room)
W_FIRST = [len(OPTS[k].replace("0", "")) for k in range(4)]                          # first room cannot hold 0

def build(dirs, k):
    """dirs: list of k*k directions. Returns adjacency lists (sets)."""
    adj = [set() for _ in range(k * k)]
    for i, d in enumerate(dirs):
        r, c = divmod(i, k); a, b = r + DR[d][0], c + DR[d][1]
        if 0 <= a < k and 0 <= b < k:
            j = a * k + b; adj[i].add(j); adj[j].add(i)
    return adj

def regions(adj):
    n = len(adj); comp = [-1] * n; sizes = []
    for s in range(n):
        if comp[s] >= 0: continue
        comp[s] = len(sizes); st = [s]; cnt = 0
        while st:
            u = st.pop(); cnt += 1
            for v in adj[u]:
                if comp[v] < 0: comp[v] = comp[s]; st.append(v)
        sizes.append(cnt)
    return comp, sizes

def longest_walk(adj):
    n = len(adj); best = 0; seen = [False] * n
    def go(u, length):
        nonlocal best
        if length > best: best = length
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True; go(v, length + 1); seen[v] = False
    for s in range(n):
        if len(adj[s]) <= 1 or all(len(adj[v]) > 0 for v in adj[s]) and len(adj[s]) == 0:
            pass
        # starting from end rooms is enough for tree parts; loops are handled by starting everywhere in small regions
        seen[s] = True; go(s, 1); seen[s] = False
    return best

def measure(dirs, k):
    adj = build(dirs, k); comp, sizes = regions(adj)
    return {"finish": comp[0] == comp[k * k - 1], "longest": longest_walk(adj), "regions": len(sizes), "largest_region": max(sizes)}

def digits_to_dirs(s): return [dir_of(int(ch)) for ch in s]

def crossings(adj, k):
    """How many separate regions join the top row to the bottom row and the left column to the right column."""
    comp, sizes = regions(adj)
    top = {comp[c] for c in range(k)}; bot = {comp[(k - 1) * k + c] for c in range(k)}
    left = {comp[r * k] for r in range(k)}; right = {comp[r * k + k - 1] for r in range(k)}
    return len(top & bot), len(left & right)

def random_prime(nd, rng):
    while True:
        x = rng.randrange(10 ** (nd - 1), 10 ** nd) | 1
        if gmpy2.is_prime(x, 25): return x

