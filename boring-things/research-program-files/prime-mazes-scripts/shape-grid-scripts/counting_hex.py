# The plain counting numbers 1 2 3 4 ... on the hexagon door grid: one whole number in each room and the number opens door (number mod 6).
# Run with: python3 counting_hex.py
import sys
sys.setrecursionlimit(100000)
from hex_compare import NBE, NBO


def build(k):
    n = k * k; adj = [set() for _ in range(n)]; outside = 0
    for i in range(n):
        r, c = divmod(i, k); d = (i + 1) % 6
        dr, dc = (NBO if c % 2 else NBE)[d]; a, b = r + dr, c + dc
        if 0 <= a < k and 0 <= b < k: j = a * k + b; adj[i].add(j); adj[j].add(i)
        else: outside += 1
    return adj, outside


def info(k):
    adj, outside = build(k); n = k * k; comp = [-1] * n; sizes = []
    for s in range(n):
        if comp[s] >= 0: continue
        st = [s]; comp[s] = len(sizes); cnt = 0
        while st:
            u = st.pop(); cnt += 1
            for v in adj[u]:
                if comp[v] < 0: comp[v] = len(sizes); st.append(v)
        sizes.append(cnt)
    top = {comp[i] for i in range(k)}; bot = {comp[(k - 1) * k + i] for i in range(k)}
    left = {comp[i * k] for i in range(k)}; right = {comp[i * k + k - 1] for i in range(k)}
    door = sum((comp[i] in bot) + (comp[(k - 1) * k + i] in top) + (comp[i * k] in right) + (comp[i * k + k - 1] in left) for i in range(k))
    # longest walk: every room opens one door so each region is a tree or a tree with one loop and a search from every room is quick
    best = 1; seen = [False] * n
    def go(u, L):
        nonlocal best
        if L > best: best = L
        for v in adj[u]:
            if not seen[v]: seen[v] = True; go(v, L + 1); seen[v] = False
    for s in range(n):
        if adj[s]: seen[s] = True; go(s, 1); seen[s] = False
    from collections import Counter
    sz = Counter(sizes)
    return dict(k=k, regions=len(sizes), big=max(sizes), walk=best, door=door, tb=len(top & bot), lr=len(left & right), three=max(sizes) + best + door, mx=2 * n + 4 * k, sizes=sz, outside=outside)


rows = [info(k) for k in range(12, 61)]
for res in range(6):
    print('--- rooms in each row leave remainder', res, 'when divided by 6')
    for d in rows:
        if d['k'] % 6 == res:
            common = ', '.join('%d rooms x %d' % (s, c) for s, c in sorted(d['sizes'].items(), key=lambda t: -t[1])[:4])
            print('%2d by %2d: regions %4d | largest %4d | longest walk %4d | top-bottom %2d side-side %2d | door points %3d of %3d | three part %4d of %4d (%4.1f%%) | most common region sizes: %s' % (
                d['k'], d['k'], d['regions'], d['big'], d['walk'], d['tb'], d['lr'], d['door'], 4 * d['k'], d['three'], d['mx'], 100 * d['three'] / d['mx'], common))
