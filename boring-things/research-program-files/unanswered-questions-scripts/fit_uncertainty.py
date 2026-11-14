# Tests getting fit uncertainties from an analytical Jacobian and comparing with scipy.optimize.curve_fit (Python forum topic 104442)
import numpy as np, scipy, time
from scipy.optimize import curve_fit, least_squares
print("scipy", scipy.__version__)
rng = np.random.default_rng(0)
def model(x, a, b, c): return a * np.exp(-b * x) + c
def jac(x, a, b, c):   # analytical derivatives of the model with respect to a, b and c
    e = np.exp(-b * x); return np.column_stack([e, -a * x * e, np.ones_like(x)])
x = np.linspace(0, 4, 200); true = (2.5, 1.3, 0.5)
y = model(x, *true) + rng.normal(scale=0.05, size=x.size)

popt, pcov = curve_fit(model, x, y, p0=(1, 1, 0))                       # the reference result
res = least_squares(lambda p: model(x, *p) - y, x0=(1, 1, 0), jac=lambda p: jac(x, *p), method="lm")
J = jac(x, *res.x); r = model(x, *res.x) - y
s2 = r @ r / (x.size - len(res.x))                                       # variance of the residuals
cov_gauss_newton = s2 * np.linalg.inv(J.T @ J)                           # covariance from the Jacobian alone

# full analytical Hessian of 0.5 * sum(r^2): J^T J plus the second derivative terms weighted by the residuals
a, b, c = res.x; e = np.exp(-b * x)
H = J.T @ J
H[0, 1] += np.sum(r * (-x * e)); H[1, 0] = H[0, 1]
H[1, 1] += np.sum(r * (a * x**2 * e))
cov_full_hessian = s2 * np.linalg.inv(H)

print("fitted parameters curve_fit:     ", np.round(popt, 6))
print("fitted parameters least_squares: ", np.round(res.x, 6))
print("standard errors curve_fit:           ", np.sqrt(np.diag(pcov)))
print("standard errors from J^T J:          ", np.sqrt(np.diag(cov_gauss_newton)))
print("standard errors from the full Hessian:", np.sqrt(np.diag(cov_full_hessian)))
print("largest relative difference J^T J versus curve_fit:      ", np.max(np.abs(cov_gauss_newton - pcov) / np.abs(pcov)))
print("largest relative difference full Hessian versus curve_fit:", np.max(np.abs(cov_full_hessian - pcov) / np.abs(pcov)))
t = time.perf_counter(); [curve_fit(model, x, y, p0=(1, 1, 0)) for _ in range(200)]; t1 = time.perf_counter() - t
t = time.perf_counter(); [curve_fit(model, x, y, p0=(1, 1, 0), jac=jac) for _ in range(200)]; t2 = time.perf_counter() - t
print(f"time for 200 fits: curve_fit with numerical derivatives {t1:.3f} s | curve_fit with jac=analytical {t2:.3f} s")
