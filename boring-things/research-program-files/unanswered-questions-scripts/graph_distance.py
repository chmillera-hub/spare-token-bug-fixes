# Three distance measures between two graphs drawn in the plane whose node labels differ (SageMath board question 88280)
import numpy as np, networkx as nx
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist, directed_hausdorff

def make(points, edges, labels):
    g = nx.Graph()
    for lab, p in zip(labels, points): g.add_node(lab, pos=tuple(p))
    g.add_edges_from((labels[a], labels[b]) for a, b in edges)
    return g

def position_distance(g1, g2):
    # pair up nodes so the total distance between partners is as small as possible, then report the mean partner distance
    n1, n2 = list(g1), list(g2)
    p1 = np.array([g1.nodes[n]["pos"] for n in n1]); p2 = np.array([g2.nodes[n]["pos"] for n in n2])
    cost = cdist(p1, p2); rows, cols = linear_sum_assignment(cost)
    mapping = {n1[r]: n2[c] for r, c in zip(rows, cols)}
    return cost[rows, cols].mean(), mapping

def edge_mismatch(g1, g2, mapping):
    # number of connections present in one graph and absent in the other after pairing up the nodes
    e1 = {frozenset((mapping[a], mapping[b])) for a, b in g1.edges if a in mapping and b in mapping}
    e2 = {frozenset(e) for e in g2.edges}
    return len(e1 ^ e2)

def hausdorff(g1, g2):
    p1 = np.array([g1.nodes[n]["pos"] for n in g1]); p2 = np.array([g2.nodes[n]["pos"] for n in g2])
    return max(directed_hausdorff(p1, p2)[0], directed_hausdorff(p2, p1)[0])

def spectral(g1, g2):
    s1 = np.sort(nx.laplacian_spectrum(g1)); s2 = np.sort(nx.laplacian_spectrum(g2))
    k = max(len(s1), len(s2)); s1 = np.pad(s1, (k - len(s1), 0)); s2 = np.pad(s2, (k - len(s2), 0))
    return float(np.linalg.norm(s1 - s2))

rng = np.random.default_rng(1)
pts = rng.random((12, 2)) * 10
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (7, 8), (9, 10), (10, 11)]     # several separate pieces on purpose
a = make(pts, edges, [f"a{i}" for i in range(12)])
perm = rng.permutation(12)
same = make(pts[perm], [(int(np.where(perm == x)[0][0]), int(np.where(perm == y)[0][0])) for x, y in edges], [f"b{i}" for i in range(12)])
moved = make(pts[perm] + rng.normal(scale=0.2, size=(12, 2)), [(int(np.where(perm == x)[0][0]), int(np.where(perm == y)[0][0])) for x, y in edges], [f"c{i}" for i in range(12)])
rewired = make(pts, edges[:-2] + [(0, 7), (4, 11)], [f"d{i}" for i in range(12)])
for name, g in (("same graph with shuffled labels", same), ("every node nudged by about 0.2", moved), ("same positions with 2 connections rewired", rewired)):
    d, mapping = position_distance(a, g)
    print(f"{name}: mean partner distance {d:.3f} | mismatched connections {edge_mismatch(a, g, mapping)} | Hausdorff distance {hausdorff(a, g):.3f} | Laplacian spectrum distance {spectral(a, g):.3f}")
