# Rechecks the figures on the page term-questions.md in the prime-richness folder.
# Run with: python3 term_questions_check.py   (needs no extra packages)
# The page asks which marks of a circle get reached when the arrow lands on each term itself
# (the term with full turns removed) and compares that with the arrow moved by each term (the running total).
import math


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


P = primes_up_to(3 * 10 ** 6)
PS = set(P)
N = 360
STEPS = 20000


def land(terms, n=N):
    return len({t % n for t in terms})


def total(terms, n=N):
    seen, pos = set(), 0
    for t in terms:
        pos = (pos + t) % n
        seen.add(pos)
    return len(seen)


def fib(k):
    out, a, b = [], 1, 1
    for _ in range(k):
        out.append(a)
        a, b = b, a + b
    return out


def fact(k):
    out, f = [], 1
    for n in range(1, k + 1):
        f *= n
        out.append(f)
    return out


rows = [
    ('counting numbers', list(range(1, STEPS))),
    ('odd numbers', [2 * n - 1 for n in range(1, STEPS)]),
    ('triangular numbers', [n * (n + 1) // 2 for n in range(1, STEPS)]),
    ('squares', [n * n for n in range(1, STEPS)]),
    ('cubes', [n ** 3 for n in range(1, STEPS)]),
    ('fourth powers', [n ** 4 for n in range(1, STEPS)]),
    ('n*n + n + 41', [n * n + n + 41 for n in range(1, STEPS)]),
    ('1 and 61 and 121 (each 60 more)', [60 * n - 59 for n in range(1, STEPS)]),
    ('Fibonacci numbers', fib(3000)),
    ('doublings', [2 ** k for k in range(0, 600)]),
    ('1 and 1*2 and 1*2*3', fact(60)),
    ('the same term 7 every time', [7] * 2000),
    ('primes', P[:STEPS]),
    ('composite numbers', [n for n in range(4, STEPS) if n not in PS]),
]
print('--- 360 marks: marks reached when the arrow lands on the term itself and when each term moves the arrow')
for name, terms in rows:
    print('%-34s literal %3d   cumulative %3d' % (name, land(terms), total(terms)))

print('--- which marks')
print('doublings', sorted({2 ** k % N for k in range(600)}))
print('1 and 1*2 and 1*2*3', sorted({f % N for f in fact(60)}), ' the product 1*2*3*4*5*6 is', math.factorial(6))
print('each 60 more', sorted({(60 * n - 59) % N for n in range(1, 400)}))

print('--- one level shift: the running totals of one row are the terms of another row')
print('odd numbers moved', total(rows[1][1]), ' squares landed', land(rows[3][1]))
print('counting numbers moved', total(rows[0][1]), ' triangular numbers landed', land(rows[2][1]))
print('same marks for odd and squares:', {t % N for t in rows[3][1]} == {sum(rows[1][1][:k]) % N for k in range(1, 800)})

print('--- primes literal on 360 marks')
pm = {p % N for p in P}
free = [r for r in range(N) if math.gcd(r, N) == 1]
print('marks reached', len(pm), ' share', 100 * len(pm) / N, ' marks that share no prime piece with 360:', len(free))
print('extra marks', sorted(pm - set(free)))
first = {}
for i, p in enumerate(P):
    first.setdefault(p % N, i + 1)
last = max(first.values())
print('every reachable mark is hit by prime number', last, 'which is', P[last - 1])
cnt = {}
for p in P[:200000]:
    cnt[p % N] = cnt.get(p % N, 0) + 1
big = [cnt[r] for r in free]
print('first 200000 primes: visits to each of the 96 marks run from', min(big), 'to', max(big), ' an even share is', 200000 / 96)
tri = {n * (n + 1) // 2 % N for n in range(1, 2000)}
print('marks shared by the 96 triangular marks and the 96 prime-free marks', len(tri & set(free)))

print('--- primes literal on other circle sizes')
for M in (2, 3, 4, 5, 6, 7, 10, 12, 30, 60, 100, 210, 256, 360, 997, 1000, 2310):
    c = len({p % M for p in P})
    print('%5d marks: %4d reached  %5.1f percent' % (M, c, 100 * c / M))

print('--- rule: marks reached = (marks sharing no prime piece with the circle size) + (number of different primes dividing the circle size)')
bad, full = 0, []
small = primes_up_to(5000)
for M in range(2, 5001):
    c = len({p % M for p in P})
    rule = sum(1 for r in range(M) if math.gcd(r, M) == 1) + sum(1 for q in small if M % q == 0)
    if c != rule:
        bad += 1
    if c == M:
        full.append(M)
print('circle sizes 2 to 5000 where the count differs from the rule:', bad)
print('circle sizes fully reached:', len(full), ' all of them prime:', all(m in PS for m in full), ' primes up to 5000:', len(small))
low = min(range(2, 5001), key=lambda M: len({p % M for p in P[:60000]}) / M)
print('lowest share for 2 to 5000 marks is at', low, 'marks:', len({p % low for p in P}), 'reached which is', 100 * len({p % low for p in P}) / low, 'percent')
