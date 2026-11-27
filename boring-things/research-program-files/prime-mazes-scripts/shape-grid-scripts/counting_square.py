# The plain counting numbers 1 2 3 4 ... on the square door grid: one whole number in each room and the number opens door (number mod 4)
# with 0 north and 1 east and 2 south and 3 west.
# Run with: python3 counting_square.py
import sys
from collections import Counter
sys.setrecursionlimit(100000)
SQ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def info(k):
    n = k * k; adj = [set() for _ in range(n)]
    for i in range(n):
        r, c = divmod(i, k); dr, dc = SQ[(i + 1) % 4]; a, b = r + dr, c + dc
        if 0 <= a < k and 0 <= b < k: j = a * k + b; adj[i].add(j); adj[j].add(i)
    comp = [-1] * n; sizes = []
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
    best = 1; seen = [False] * n
    def go(u, L):
        nonlocal best
        if L > best: best = L
        for v in adj[u]:
            if not seen[v]: seen[v] = True; go(v, L + 1); seen[v] = False
    for s in range(n):
        if adj[s]: seen[s] = True; go(s, 1); seen[s] = False
    return dict(k=k, regions=len(sizes), big=max(sizes), walk=best, door=door, tb=len(top & bot), lr=len(left & right), three=max(sizes) + best + door, mx=2 * n + 4 * k, sizes=Counter(sizes))


rows = [info(k) for k in range(12, 61)]
for res in range(4):
    print('--- rooms in each row leave remainder', res, 'when divided by 4')
    for d in rows:
        if d['k'] % 4 == res and (d['k'] < 30 or d['k'] > 55):
            common = ', '.join('%d rooms x %d' % (s, c) for s, c in sorted(d['sizes'].items(), key=lambda t: -t[1])[:4])
            print('%2d by %2d: regions %4d | largest %4d | longest walk %4d | top-bottom %2d side-side %2d | door points %3d of %3d | three part %4d of %4d (%4.1f%%) | most common region sizes: %s' % (
                d['k'], d['k'], d['regions'], d['big'], d['walk'], d['tb'], d['lr'], d['door'], 4 * d['k'], d['three'], d['mx'], 100 * d['three'] / d['mx'], common))
