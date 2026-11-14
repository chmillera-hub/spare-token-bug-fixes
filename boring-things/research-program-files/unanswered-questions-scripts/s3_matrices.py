# Builds the map from the symmetric group S3 to 2 by 2 matrices (rotations and reflections of a triangle) and checks every product
import sympy as sp
from sympy.combinatorics import Permutation
from sympy.combinatorics.named_groups import SymmetricGroup
G = SymmetricGroup(3)
corners = [sp.Matrix([sp.cos(2 * sp.pi * k / 3), sp.sin(2 * sp.pi * k / 3)]) for k in range(3)]   # corners 0, 1, 2 of an equilateral triangle
def matrix_of(p):
    # the unique matrix that sends corner k to corner p(k)
    src = sp.Matrix.hstack(corners[0], corners[1]); dst = sp.Matrix.hstack(corners[p(0)], corners[p(1)])
    return sp.simplify(dst * src.inv())
table = {p: matrix_of(p) for p in G.elements}
print("number of group elements:", len(table))
print("each matrix moves every corner k to corner p(k):", all(sp.simplify(table[p] * corners[k] - corners[p(k)]) == sp.zeros(2, 1) for p in table for k in range(3)))
# sympy writes p*q for "first p then q", so the matching matrix product is M(q) * M(p)
print("the map respects multiplication for all 36 pairs:", all(sp.simplify(table[p * q] - table[q] * table[p]) == sp.zeros(2) for p in table for q in table))
print("all six matrices are different:", len({tuple(m) for m in table.values()}) == 6)
print("every matrix keeps lengths (M^T M = identity):", all(sp.simplify(m.T * m) == sp.eye(2) for m in table.values()))
rot = Permutation([1, 2, 0]); ref = Permutation([0, 2, 1])
print("matrix of the 3-cycle 0->1->2->0 (a rotation by 120 degrees):", table[rot].tolist(), "| determinant", table[rot].det())
print("matrix of the swap of corners 1 and 2 (a reflection across the x axis):", table[ref].tolist(), "| determinant", table[ref].det())
print("traces by cycle type (2 for the identity, 0 for swaps, -1 for 3-cycles):", sorted((len(p.cyclic_form[0]) if p.cyclic_form else 1, sp.simplify(m.trace())) for p, m in table.items()))
