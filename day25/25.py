import sys
from collections import defaultdict

import networkx as nx


def solve_p1():
    lines = open(sys.argv[1]).read().strip().split("\n")
    D = defaultdict(list)
    pairs = set()
    for line in lines:
        source, conn = line.split(":")
        conn = conn.strip().split(" ")
        D[source].extend(conn)
        for i in conn:
            D[i].append(source)
        pairs.update(((source, c) for c in conn))
    pairs = tuple(pairs)

    G = nx.DiGraph()
    for key, val in D.items():
        for v in val:
            G.add_edge(key, v, capacity=1.0)
            G.add_edge(v, key, capacity=1.0)

    for x in [tuple(D.keys())[0]]:
        for y in D.keys():
            if x != y:
                cv, (L, R) = nx.minimum_cut(G, x, y)
                if cv == 3:
                    print(len(L) * len(R))
                    break


solve_p1()
