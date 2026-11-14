# Checks that mpmath (a library that ships inside SageMath) evaluates associated Legendre functions outside the interval (-1, 1)
# against the hypergeometric formula for Q (DLMF 14.3.7) and against known closed forms   (SageMath board question 88040)
import mpmath as mp
mp.mp.dps = 30
def q_hyper(nu, mu, x):
    # Q^mu_nu(x) for x > 1 from DLMF 14.3.7 with the regularized hypergeometric function written out
    f = mp.hyp2f1(mu / 2 + nu / 2 + 1, mu / 2 + nu / 2 + mp.mpf(1) / 2, nu + mp.mpf(3) / 2, 1 / x**2) / mp.gamma(nu + mp.mpf(3) / 2)
    return mp.exp(1j * mp.pi * mu) * mp.gamma(nu + mu + 1) * mp.sqrt(mp.pi) * (x**2 - 1) ** (mu / 2) / (2 ** (nu + 1) * x ** (nu + mu + 1)) * f
for nu, mu, x in ((0, 0, 2), (1, 0, 3), (2, 1, 1.5), (mp.mpf("2.5"), mp.mpf("0.5"), 4), (3, 2, 10)):
    lib = mp.legenq(nu, mu, x, type=3)
    ref = q_hyper(mp.mpf(nu), mp.mpf(mu), mp.mpf(x))
    print(f"Q: nu = {nu}, mu = {mu}, x = {x} | mpmath type=3: {mp.nstr(lib, 15)} | hypergeometric formula: {mp.nstr(ref, 15)} | difference {mp.nstr(abs(lib - ref), 3)}")
x = mp.mpf(2)
print("Q_0(2) equals 0.5*log((x+1)/(x-1)):", mp.nstr(abs(mp.legenq(0, 0, x, type=3) - mp.log((x + 1) / (x - 1)) / 2), 3))
print("Q_1(2) equals (x/2)*log((x+1)/(x-1)) - 1:", mp.nstr(abs(mp.legenq(1, 0, x, type=3) - (x / 2 * mp.log((x + 1) / (x - 1)) - 1)), 3))
print("P^1_1(2) equals sqrt(x^2-1):", mp.nstr(abs(mp.legenp(1, 1, x, type=3) - mp.sqrt(x**2 - 1)), 3))
print("P^2_2(2) equals 3*(x^2-1):", mp.nstr(abs(mp.legenp(2, 2, x, type=3) - 3 * (x**2 - 1)), 3))
print("Ferrers version (type=2) at x = 0.3 for comparison: P^1_1 =", mp.nstr(mp.legenp(1, 1, 0.3, type=2), 12), "| -sqrt(1-x^2) =", mp.nstr(-mp.sqrt(1 - mp.mpf("0.3")**2), 12))
