# Numerical check of the step in Riemann's 1859 paper asked about on the Wikipedia mathematics reference desk
# Claim: 2 sin(pi s) Gamma(s) zeta(s) = i * integral over a contour that comes in from +infinity just above the
# positive real axis, circles the origin counterclockwise, and goes back out just below the axis, of (-x)^(s-1)/(e^x-1) dx
# where (-x)^(s-1) = exp((s-1) log(-x)) and log(-x) is real for negative x.   (Riemann's Pi(s-1) equals Gamma(s).)
from mpmath import mp, mpf, mpc, quad, exp, log, sin, pi, gamma, zeta, inf
mp.dps = 25
def f(x, s):
    return exp((s - 1) * log(-x)) / (exp(x) - 1)
def contour(s, r=mpf(1), eps=mpf("1e-12")):
    # upper edge: from +infinity to r (x = t + i*eps), circle |x| = r counterclockwise from angle 0+ to 2pi-, lower edge: r to +infinity
    upper = quad(lambda t: f(mpc(t, eps), s), [inf, 20, r])
    circle = quad(lambda th: f(r * exp(1j * th), s) * 1j * r * exp(1j * th), [eps, pi / 2, pi, 3 * pi / 2, 2 * pi - eps])
    lower = quad(lambda t: f(mpc(t, -eps), s), [r, 20, inf])
    return upper + circle + lower
for s in (mpf("2.5"), mpf("3.7"), mpc("1.5", "2.0"), mpf("-1.5"), mpc("0.5", "14.134725")):
    left = 2 * sin(pi * s) * gamma(s) * zeta(s)
    right = 1j * contour(s)
    print("s =", s, "| left side", mp.nstr(left, 12), "| right side", mp.nstr(right, 12), "| difference", mp.nstr(abs(left - right), 3))
