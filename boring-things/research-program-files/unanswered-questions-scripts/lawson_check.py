# Checks the surface asked about on the Wikipedia mathematics reference desk (is it Lawson's Klein bottle?)
import numpy as np
rng = np.random.default_rng(0)
def asked(t, p):   # the formula in the question
    return np.array([np.cos(t)*np.cos(p), np.cos(t)*np.sin(p), np.sin(t)*np.cos(p), np.sin(t)*np.sin(p)])
def tau(m, k, x, y):  # Lawson's family
    return np.array([np.cos(m*x)*np.cos(y), np.sin(m*x)*np.cos(y), np.cos(k*x)*np.sin(y), np.sin(k*x)*np.sin(y)])
t, p = rng.uniform(0, 2*np.pi, (2, 100000))
P = asked(t, p)
print("asked formula: max |w z - x y| =", np.abs(P[0]*P[3] - P[1]*P[2]).max(), "(zero means every point sits on the quadric w z = x y)")
print("asked formula equals tau(1,1) with x = phi and y = theta: max difference", np.abs(P - tau(1, 1, p, t)).max())
print("asked formula: point at (theta+pi, phi+pi) equals point at (theta, phi): max difference", np.abs(asked(t+np.pi, p+np.pi) - P).max())
K = tau(2, 1, t, p)
print("tau(2,1): point at (x+pi, -y) equals point at (x, y): max difference", np.abs(tau(2, 1, t+np.pi, -p) - K).max())
# orientation test: does the identification reverse orientation of the (x, y) parameter plane?
print("tau(2,1) identification (x, y) -> (x+pi, -y) has Jacobian determinant", np.linalg.det(np.array([[1, 0], [0, -1]])), "(negative means orientation reversing, so the quotient is a Klein bottle)")
print("tau(1,1) identification (theta, phi) -> (theta+pi, phi+pi) has Jacobian determinant", np.linalg.det(np.eye(2)), "(positive means orientation preserving, so the quotient is a torus)")
