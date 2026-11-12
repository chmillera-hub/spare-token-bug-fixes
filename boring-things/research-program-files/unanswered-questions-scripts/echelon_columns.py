# Row-reduces a k by n matrix so that the identity matrix appears on any chosen k columns (SageMath board question 83654)
import random, sympy as sp
random.seed(3)

def echelon_on(G, cols):
    # multiply G from the left by the inverse of the k by k block made of the chosen columns
    k = G.rows
    block = G.extract(list(range(k)), list(cols))
    if block.det() == 0:
        raise ValueError("the chosen columns are linearly dependent, so no such form exists")
    return block.inv() * G

k, n = 3, 7
G = sp.Matrix(k, n, lambda i, j: random.randint(-4, 4))
print("G =", G.tolist(), "| rank", G.rank())
for cols in ((4, 5, 6), (1, 3, 6), (6, 0, 2)):
    E = echelon_on(G, cols)
    print("chosen columns", cols, "| identity on those columns:", E.extract(list(range(k)), list(cols)) == sp.eye(k), "| same row space as G:", sp.Matrix.vstack(G, E).rank() == k)
print("last-3-columns result:", echelon_on(G, (4, 5, 6)).tolist())

# the same idea over a finite field with p elements (common in coding theory): do the arithmetic modulo p
def echelon_on_mod(G, cols, p):
    k = G.rows
    block = G.extract(list(range(k)), list(cols))
    return (block.inv_mod(p) * G).applyfunc(lambda v: v % p)
p = 2
while True:
    G2 = sp.Matrix(4, 8, lambda i, j: random.randint(0, 1))
    if G2.extract(list(range(4)), [4, 5, 6, 7]).det() % 2 == 1: break
E2 = echelon_on_mod(G2, (4, 5, 6, 7), p)
print("over the field with 2 elements: G =", G2.tolist())
print("result:", E2.tolist(), "| identity on the last 4 columns:", E2.extract([0, 1, 2, 3], [4, 5, 6, 7]) == sp.eye(4))
dep = sp.Matrix([[1, 2, 3, 4], [2, 4, 1, 1]])
try: echelon_on(dep, (0, 1))
except ValueError as e: print("columns 0 and 1 of [[1,2,3,4],[2,4,1,1]]:", e)
