# Compares the door maze on square rooms (0 opens north then clockwise in 4 steps) with the door maze on hexagon rooms
# (0 opens north then clockwise in 6 steps: north, northeast, southeast, south, southwest, northwest).
# Hexagon layout: same number of rooms in each row and column and every second column sits half a room lower.
# Run with: python3 hex_compare.py
import random, sys, json
sys.setrecursionlimit(10000)
SQ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
NBE = [(-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1)]
NBO = [(-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def build(digs, k, hexa):
    adj = [set() for _ in range(k * k)]
    for i, n in enumerate(digs[:k * k]):
        r, c = divmod(i, k)
        if hexa: dr, dc = (NBO if c % 2 else NBE)[n % 6]
        else: dr, dc = SQ[n % 4]
        a, b = r + dr, c + dc
        if 0 <= a < k and 0 <= b < k:
            j = a * k + b; adj[i].add(j); adj[j].add(i)
    return adj


def score(adj, k):
    n = k * k; comp = [-1] * n; sizes = []
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
    return {'regions': len(sizes), 'big': max(sizes), 'walk': best, 'door': door, 'tb': len(top & bot), 'lr': len(left & right), 'three': max(sizes) + best + door}


def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True


def summarize(label, numbers, k):
    out = {}
    for hexa in (False, True):
        tot = {'big': 0, 'walk': 0, 'door': 0, 'three': 0, 'regions': 0}; full = 0; nodoor = 0
        for v in numbers:
            digs = [int(ch) for ch in str(v)]
            sc = score(build(digs, k, hexa), k)
            for key in tot: tot[key] += sc[key]
            full += sc['walk'] == k * k; nodoor += sc['big'] == 1
        m = len(numbers); mx = 2 * k * k + 4 * k
        out['hexagons' if hexa else 'squares'] = dict(avg_regions=round(tot['regions'] / m, 2), avg_largest=round(tot['big'] / m, 2), avg_walk=round(tot['walk'] / m, 2), avg_door=round(tot['door'] / m, 2),
                                                       avg_three_pct=round(100 * tot['three'] / m / mx, 1), full_hallway_pct=round(100 * full / m, 3), no_join_pct=round(100 * nodoor / m, 2))
    print(label, '(', len(numbers), 'numbers on', k, 'by', k, 'rooms )')
    for kind, d in out.items(): print('   %-9s' % kind, d)


if __name__ == '__main__':
    random.seed(7)
    p4 = [n for n in range(1000, 10000) if is_prime(n)]
    summarize('every prime with 4 digits', p4, 2)
    summarize('every number with 4 digits', list(range(1000, 10000)), 2)
    p9 = []
    while len(p9) < 60000:
        v = random.randrange(10 ** 8, 10 ** 9) | 1
        if is_prime(v): p9.append(v)
    summarize('random primes with 9 digits', p9, 3)
    summarize('random numbers with 9 digits', [random.randrange(10 ** 8, 10 ** 9) for _ in range(60000)], 3)
    summarize('random numbers with 16 digits', [random.randrange(10 ** 15, 10 ** 16) for _ in range(30000)], 4)
    summarize('random numbers with 36 digits', [random.randrange(10 ** 35, 10 ** 36) for _ in range(6000)], 6)
    summarize('random numbers with 100 digits', [random.randrange(10 ** 99, 10 ** 100) for _ in range(1500)], 10)
    # door share by direction for plain digits
    print('share of the ten digits that open each hexagon door: north 2 northeast 2 southeast 2 south 2 southwest 1 northwest 1')
    tests = ['1087', '102002003', '8856673763365447', '6373956411280594', '1111111112111111112201111112220011112222000112222200001322220000333222000333332200333333320333333333', '2363667423305504']
    ref = {t: score(build([int(c) for c in t], int(len(t) ** 0.5), True), int(len(t) ** 0.5)) for t in tests}
    json.dump(ref, open('ref.json', 'w')); print(ref['1087'], ref['102002003'])
