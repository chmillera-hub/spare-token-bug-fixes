# Checks the geometry of the script posted in matplotlib forum topic 26068 (circle inscribed between MA, MB and arc AB)
import numpy as np
r = 2.0
O = np.array([0.0, 0.0]); A = np.array([r, 0.0]); M = np.array([0.0, r / 2])
def rot(deg):
    t = np.deg2rad(deg); return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
vec_MA = A - M
u = rot(60) @ vec_MA / np.linalg.norm(vec_MA)
b = 2 * M @ u; c = M @ M - r**2
s = max(x for x in ((-b + np.sqrt(b*b - 4*c)) / 2, (-b - np.sqrt(b*b - 4*c)) / 2) if x > 0)
B = M + s * u
ub = rot(30) @ vec_MA; ub /= np.linalg.norm(ub)
a = 3 / 4; bc = 2 * (M @ ub) + r; c = M @ M - r**2
s = (-bc + np.sqrt(bc*bc - 4*a*c)) / (2*a); rho = s / 2; I = M + s * ub
def dist_to_line(P, Q, X):
    d = (Q - P) / np.linalg.norm(Q - P); w = X - P; return abs(d[0]*w[1] - d[1]*w[0])
ang = lambda P: np.degrees(np.arctan2(P[1], P[0]))
print("B =", np.round(B, 6), "| distance of B from O:", round(float(np.linalg.norm(B)), 12), "| angle AMB in degrees:", round(float(np.degrees(np.arccos((A - M) @ (B - M) / np.linalg.norm(A - M) / np.linalg.norm(B - M)))), 9))
print("I =", np.round(I, 6), "| radius rho =", round(float(rho), 6))
print("distance from I to line MA minus rho:", dist_to_line(M, A, I) - rho)
print("distance from I to line MB minus rho:", dist_to_line(M, B, I) - rho)
print("distance from I to O plus rho minus r:", np.linalg.norm(I) + rho - r)
T = I / np.linalg.norm(I) * r
print("touch point on the big circle sits at angle", round(float(ang(T)), 4), "degrees | arc AB runs from", round(float(ang(A)), 4), "to", round(float(ang(B)), 4), "degrees | touch point lies on arc AB:", ang(A) <= ang(T) <= ang(B))
for name, P, Q in (("MA", M, A), ("MB", M, B)):
    d = (Q - P) / np.linalg.norm(Q - P); t = (I - P) @ d
    print("touch point on", name, "lies between the two end points:", 0 <= t <= np.linalg.norm(Q - P))
