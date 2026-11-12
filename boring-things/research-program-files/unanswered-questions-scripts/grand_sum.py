# Checks that the sum of all entries of the n-fold tensor power of [z^2, c] equals (z^2 + c)^n
import sympy as sp
from sympy.physics.quantum import TensorProduct
z, c = sp.symbols("z c")
v = sp.Matrix([[z**2, c]])
t = v
for n in range(1, 8):
    total = sp.expand(sum(t))
    print("n =", n, "| entries:", len(t), "| sum of all entries equals (z^2+c)^n:", sp.expand((z**2 + c)**n - total) == 0)
    t = TensorProduct(t, v)
# Because the sum equals (z^2 + c)^n the behaviour for large n depends only on the single number w = z^2 + c
for w in (sp.Rational(1, 2), sp.I / 2, sp.Integer(1), sp.Integer(-1), sp.Rational(3, 2)):
    print("z^2 + c =", w, "| size |z^2+c| =", sp.Abs(w), "| values for n = 1, 2, 3, 50:", [sp.nsimplify(w**k) if k < 4 else sp.N(w**k, 5) for k in (1, 2, 3, 50)])
