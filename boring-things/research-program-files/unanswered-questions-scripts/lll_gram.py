# Shows what the PARI functions qflllgram and qflll return (SageMath board question 83810). Needs the cypari package.
from cypari import pari
import numpy as np
print("PARI version", pari("version()"))
np.set_printoptions(suppress=True, precision=4)

def gram(B): return B.T @ B                                  # columns of B are the basis vectors
def pari_mat(A): return pari("[" + ";".join(",".join(repr(float(v)) for v in row) for row in A) + "]")
def np_mat(M):
    r, c = int(pari.matsize(M)[0]), int(pari.matsize(M)[1])
    return np.array([[float(M[i, j]) for j in range(c)] for i in range(r)])

# case 1: a basis that is already reduced (short and nearly at right angles)
B1 = np.array([[1.0, 0.2], [0.1, 1.1], [0.0, 0.3]])
T1 = np_mat(pari.qflllgram(pari_mat(gram(B1))))
print("case 1 (already reduced basis): qflllgram(Gram) =", T1.tolist(), "-> identity:", np.array_equal(T1, np.eye(2)))

# case 2: the same lattice described by a skewed basis
U = np.array([[1.0, 7.0], [0.0, 1.0]])                        # a whole-number change of basis with determinant 1
B2 = B1 @ U
G2 = gram(B2)
T2 = np_mat(pari.qflllgram(pari_mat(G2)))
print("case 2 (skewed basis): qflllgram(Gram) =", T2.tolist(), "| determinant", round(float(np.linalg.det(T2))))
print("   lengths of the skewed basis vectors:", np.round(np.linalg.norm(B2, axis=0), 3), "| lengths after multiplying by the returned matrix:", np.round(np.linalg.norm(B2 @ T2, axis=0), 3))
print("   reduced Gram matrix T^T * G * T:", np.round(T2.T @ G2 @ T2, 4).tolist())

# what happens when the Gram matrix is handed to qflll, which expects the basis vectors themselves
T3 = np_mat(pari.qflll(pari_mat(G2)))
T4 = np_mat(pari.qflll(pari_mat(B2)))
print("qflll(basis) equals qflllgram(Gram):", np.array_equal(T4, T2), "| qflll(Gram) =", T3.tolist(), "| equals qflllgram(Gram):", np.array_equal(T3, T2))
print("   qflll(Gram) treats the columns of the Gram matrix as if they were basis vectors, which is a different lattice")
