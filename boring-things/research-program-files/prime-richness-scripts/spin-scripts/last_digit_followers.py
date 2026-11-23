# For two million primes after 2 and 3 and 5: how often a prime with a given last digit is followed by a prime with each last digit.
# A fair coin would give 25 percent for each. Needs numpy.
import numpy as np
LIM = 33 * 10 ** 6
s = np.ones(LIM + 1, dtype=bool)
s[:2] = False
for i in range(2, int(LIM ** 0.5) + 1):
    if s[i]:
        s[i * i::i] = False
P = np.nonzero(s)[0][3:2000003]
d = P % 10
for a in (1, 3, 7, 9):
    m = d[:-1] == a
    nxt = d[1:][m]
    print('last digit', a, ' count', int(m.sum()), ' next last digit shares in percent', {b: round(100 * float((nxt == b).mean()), 1) for b in (1, 3, 7, 9)})
