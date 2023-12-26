import sys
from collections import defaultdict
from functools import reduce
from itertools import combinations, permutations
from pprint import pprint
from time import time


def solve(connections, D, fst, snd, third):
    illegal_cons = [*fst, *snd, *third]
    conn_len = len(connections)
    visited = set()
    k = 0
    group_lengths = []

    while [c for c in connections if c not in visited]:
        count = 0
        curr = [c for c in connections if c not in visited][0]

        if k >= conn_len and curr in visited:
            break

        Q = [curr]
        while Q:
            curr = Q.pop()

            if curr in visited:
                continue
            visited.add(curr)
            count += 1
            Q.extend(
                (
                    i
                    for i in D[curr]
                    if (curr not in illegal_cons or i not in illegal_cons)
                    and i not in visited
                )
            )
        if count == 1:
            return 0
        group_lengths.append(count)
    if len(group_lengths) > 1:
        print(group_lengths)
        return reduce(lambda x, n: x * n, group_lengths)
    return 0


def solve_p1():
    lines = open(sys.argv[1]).read().strip().split("\n")
    D = defaultdict(set)
    connections = set()
    pairs = set()
    for line in lines:
        source, conn = line.split(":")
        conn = conn.strip().split(" ")
        D[source].update(conn)
        for i in conn:
            D[i].add(source)
        connections.add(source)
        connections.update(set(conn))
        pairs.update(((source, c) for c in conn))
    connections = tuple(connections)
    pairs = tuple(pairs)
    pprint(D)
    pprint(pairs)
    p1 = 0
    searched = 0
    for i in range(len(pairs)):
        c1 = pairs[i]
        for j in range(i + 1, len(pairs)):
            c2 = pairs[j]
            if c1[0] in c2 or c1[1] in c2:
                continue
            for k in range(j + 1, len(pairs)):
                c3 = pairs[k]
                if c1[0] in c3 or c1[1] in c3:
                    continue
                if c2[0] in c3 or c2[1] in c3:
                    continue

                answer = solve(connections, D, c1, c2, c3)
                searched += 1
                print(searched)
                if answer != 0:
                    p1 = answer
                    print("p1", answer)
                    return 0
    print(searched, len(list(combinations(pairs, 3))))
    # print(sums)

    print("p1", p1)


solve_p1()
