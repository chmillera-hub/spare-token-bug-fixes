# Restricted matching number of a graph: a fast method checked against brute force (SageMath board question 83031)
# Two edges form a gap when they share no vertex and no edge of the graph joins a vertex of one to a vertex of the other.
# A restricted matching is a matching in which one chosen edge forms a gap with every other edge of the matching.
import itertools, random, networkx as nx

def restricted_matching_number(G):
    best, witness = 0, None
    for u, v in G.edges:
        blocked = set(G[u]) | set(G[v]) | {u, v}                 # the chosen edge and everything touching it
        rest = G.subgraph(set(G) - blocked)
        m = nx.max_weight_matching(rest, maxcardinality=True)    # the other edges only need to be a matching
        if 1 + len(m) > best:
            best, witness = 1 + len(m), [(u, v)] + [tuple(e) for e in m]
    return best, witness

def is_gap(G, e, f):
    return not (set(e) & set(f)) and not any(G.has_edge(a, b) for a in e for b in f)

def brute_force(G):
    edges = list(G.edges); best = 0
    for k in range(1, len(G) // 2 + 1):
        for M in itertools.combinations(edges, k):
            used = [x for e in M for x in e]
            if len(set(used)) != 2 * k: continue                  # not a matching
            if any(all(is_gap(G, e, f) for f in M if f != e) for e in M): best = k
    return best

random.seed(5); checked = 0
for trial in range(300):
    n = random.randint(2, 9)
    G = nx.gnp_random_graph(n, random.choice([0.2, 0.35, 0.5]), seed=random.randint(0, 10**6))
    if G.number_of_edges() == 0: continue
    fast, w = restricted_matching_number(G)
    assert fast == brute_force(G), (G.edges, fast)
    checked += 1
print("random graphs checked against brute force:", checked, "| all equal: True")
for name, G in (("path with 7 vertices", nx.path_graph(7)), ("cycle with 8 vertices", nx.cycle_graph(8)), ("complete graph with 6 vertices", nx.complete_graph(6)),
                ("Petersen graph", nx.petersen_graph()), ("5 by 5 grid", nx.grid_2d_graph(5, 5)), ("star with 6 leaves", nx.star_graph(6))):
    r, w = restricted_matching_number(G)
    print(f"{name}: restricted matching number {r} | ordinary matching number {len(nx.max_weight_matching(G, maxcardinality=True))}")
import time
G = nx.gnp_random_graph(300, 0.02, seed=1); t = time.time(); r, _ = restricted_matching_number(G)
print(f"random graph with 300 vertices and {G.number_of_edges()} edges: restricted matching number {r} in {time.time() - t:.1f} s")
