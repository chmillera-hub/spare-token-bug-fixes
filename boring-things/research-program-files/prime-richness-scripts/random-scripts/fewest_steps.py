# How few steps can fill both circles? Checks the sequence 0 + 1 - 2 + 3 - 4 and searches small circles for the true minimum.
# Run with: python3 fewest_steps.py
import itertools


def steps_to_fill(term, N, cap=None):
    cap = cap or 10 * N + 10
    lit, cum, pos, fl, fc = set(), set(), 0, None, None
    for k in range(1, cap + 1):
        t = term(k) % N
        lit.add(t); pos = (pos + t) % N; cum.add(pos)
        if fl is None and len(lit) == N: fl = k
        if fc is None and len(cum) == N: fc = k
        if fl and fc: break
    return fl, fc


alt = lambda k: k if k % 2 else -k                    # 1 - 2 + 3 - 4
zalt = lambda k: 0 if k == 1 else ((k - 1) if (k - 1) % 2 else -(k - 1))   # 0 + 1 - 2 + 3 - 4
print('--- 1 - 2 + 3 - 4 and 0 + 1 - 2 + 3 - 4: steps to fill the literal circle and the cumulative circle')
for N in (10, 11, 360, 361, 1000, 4999, 5000):
    print(N, 'without the 0:', steps_to_fill(alt, N), ' with the 0 in front:', steps_to_fill(zalt, N))
ev = [N for N in range(2, 5001, 2) if steps_to_fill(zalt, N) != (N, N)]
od = [N for N in range(3, 5001, 2) if steps_to_fill(zalt, N) != (2 * N - 1, N)]
print('even sizes up to 5000 where 0 + 1 - 2 + 3 - 4 does not finish both circles in exactly N steps:', len(ev))
print('odd sizes up to 5000 where 0 + 1 - 2 + 3 - 4 does not take 2N - 1 steps (literal) and N steps (cumulative):', len(od))


def best(N, extra):
    # fewest steps over every possible sequence of marks, by search (small N only)
    L = N + extra
    for seq in itertools.product(range(N), repeat=L):
        if len(set(seq)) < N: continue
        pos, cum = 0, set()
        for t in seq: pos = (pos + t) % N; cum.add(pos)
        if len(cum) == N: return seq
    return None


print('--- true minimum by trying every sequence on small circles')
for N in (2, 3, 4, 5, 6, 7):
    for extra in (0, 1, 2):
        s = best(N, extra)
        if s:
            print(N, 'marks: fewest steps', N + extra, ' one sequence that does it:', s); break
