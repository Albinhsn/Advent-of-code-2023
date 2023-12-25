import sys
from pprint import pprint


def solve_p1():
    lines = open(sys.argv[1]).read().strip().split("\n")
    D = {}
    connections = set()
    for line in lines:
        source, conn = line.split(":")
        conn = conn.strip().split(" ")
        D[source] = conn
        connections.add(source)
        connections.update(set(conn))
    connections = list(connections)
    pprint(D)
    groups = []
    for i in range(len(connections)):
        for j in range(i + 1, len(connections)):
            fst, snd = connections[i], connections[j]
            Q = []
