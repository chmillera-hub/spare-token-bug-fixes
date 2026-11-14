# Galois group of the field made by the eigenvalues of the 5-cycle graph, as a permutation group (SageMath board question 87751)
import networkx as nx, sympy as sp
x = sp.symbols("x")
A = sp.Matrix(nx.to_numpy_array(nx.cycle_graph(5)).astype(int))
char = sp.factor(A.charpoly(x).as_expr())
print("characteristic polynomial of the 5-cycle:", char)
print("eigenvalues:", A.eigenvals())
for factor, power in sp.factor_list(char)[1]:
    p = sp.Poly(factor, x)
    if p.degree() < 2:
        print("factor", factor, "| degree 1 so the root is a rational number and adds nothing to the field"); continue
    G, alt = p.galois_group()
    print("factor", factor, "| Galois group generators:", G.generators, "| order:", G.order(), "| abelian:", G.is_abelian)
r = sp.sqrt(5)
print("the two irrational eigenvalues are (-1 + sqrt(5))/2 and (-1 - sqrt(5))/2, so the field is the rationals with sqrt(5) added (degree 2)")
print("the one non-trivial symmetry swaps the two eigenvalues:", sp.simplify(((-1 + r) / 2).subs(r, -r) - (-1 - r) / 2) == 0)
