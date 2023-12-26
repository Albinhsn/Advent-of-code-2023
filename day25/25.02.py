import sys
from collections import defaultdict
from functools import reduce
from itertools import combinations, permutations
from pprint import pprint


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


def bfs(source, needle, illegal, D):
    visited = set()
    visited.add(source)
    Q = [(d, []) for d in D[source] if d != needle]
    while Q:
        curr, path = Q.pop()
        print(f"curr: {curr}, path: {path}, visited: {visited}")
        if curr in visited or curr in illegal:
            continue
        if curr == needle:
            return path
        visited.add(curr)
        path.append(curr)
        Q.extend(
            (
                (i, path.copy())
                for i in D[curr]
                if (i not in illegal and i not in visited)
            )
        )
    return []


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
    pairs = [("bvb", "cmg")]
    for i in range(len(pairs)):
        source, needle = pairs[i]
        print(source, "->", needle)
        # BFS from first to second
        illegal = [source]
        path = bfs(source, needle, illegal, D)
        # BFS again and remove everything from first path
        illegal = [i for i in path if i not in [source, needle]]
        print(path)
        exit(1)
        if not path:
            print("Failed after first")
            continue
        path = bfs(source, needle, illegal, D)

        # BFS a third time and check if there is no path
        illegal.extend([i for i in path if i not in [source, needle]])
        print(path, illegal)
        if not path:
            print("Failed after second")
            continue
        path = bfs(source, needle, illegal, D)
        print(path)
        # if there isn't check all pairs possible from the paths
        if not path:
            print(illegal)
            exit(1)

    # print(sums)

    print("p1", p1)


solve_p1()
