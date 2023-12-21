import sys
import time
from collections import defaultdict, deque
from copy import deepcopy


def solve_p1():
    lines = open(sys.argv[1]).read().strip().split("\n")
    x, y = [
        [(idx, i) for idx, x in enumerate(y) if x == "S"][0]
        for i, y in enumerate(lines)
        if "S" in y
    ][0]
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    Q = deque([(x, y)])
    STEPS = 64
    for _ in range(STEPS):
        arr = set()
        while Q:
            x, y = Q.popleft()

            for xx, yy in XY:
                if (
                    x + xx < 0
                    or x + xx >= len(lines[0])
                    or y + yy < 0
                    or y + yy >= len(lines)
                    or lines[y + yy][x + xx] == "#"
                ):
                    continue
                arr.add((x + xx, y + yy))
        Q.extend(arr)
    print("p1", len(Q))


def solve_p2():
    time1 = time.time()
    lines = open(sys.argv[1]).read().strip().split("\n")
    x, y = [
        [(idx, i) for idx, x in enumerate(y) if x == "S"][0]
        for i, y in enumerate(lines)
        if "S" in y
    ][0]
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    X, Y = len(lines[0]), len(lines)
    STEPS = 500
    plots1 = defaultdict(set)
    plots2 = defaultdict(set)
    plots2[(x, y)].add((0, 0))
    neighbours = defaultdict(set)
    p2 = 1
    for i in range(Y):
        for j in range(X):
            for xx, yy in XY:
                tmp_x, tmp_y = j + xx, i + yy
                gdx, gdy = (0, 0)
                if tmp_y < 0:
                    tmp_y = Y + tmp_y
                    gdy = -1
                elif tmp_y >= Y:
                    tmp_y = tmp_y - Y
                    gdy = 1
                if tmp_x < 0:
                    tmp_x = X + tmp_x
                    gdx = -1
                elif tmp_x >= X:
                    tmp_x = tmp_x - X
                    gdx = 1
                if lines[tmp_x][tmp_y] == "#":
                    continue
                neighbours[(j, i)].add(((tmp_x, tmp_y), gdx, gdy))
    visited = set()
    previous = {}
    for steps in range(STEPS // 2):
        tmp_dict = defaultdict(set)
        for pos, grids in plots2.items():
            for xy, gdx, gdy in neighbours[pos]:
                tmp_dict[xy].update(
                    (i[0] + gdx, i[1] + gdy)
                    for i in grids
                    if (i[0] + gdx, i[1] + gdy) not in plots1[xy]
                )
        if tuple(tmp_dict.keys()) in visited:
            # print(previous[tuple(tmp_dict.keys())]["steps"], steps)
            prev = previous[tuple(tmp_dict.keys())]["dict"]
            print([len(tmp_dict[key]) - len(prev[key]) for key in tmp_dict])
            print("-"*15)
        visited.add(tuple(tmp_dict.keys()))
        previous[tuple(tmp_dict.keys())] = {"steps": steps, "dict": deepcopy(tmp_dict)}
        plots1 = tmp_dict

        tmp_dict = defaultdict(set)
        for pos, grids in plots1.items():
            for xy, gdx, gdy in neighbours[pos]:
                tmp_dict[xy].update(
                    (i[0] + gdx, i[1] + gdy)
                    for i in grids
                    if (i[0] + gdx, i[1] + gdy) not in plots2[xy]
                )
        p2 += sum(len(i) for i in tmp_dict.values())
        if tuple(tmp_dict.keys()) in visited:
            # print(previous[tuple(tmp_dict.keys())], steps)
            prev = previous[tuple(tmp_dict.keys())]["dict"]
            print([len(tmp_dict[key]) - len(prev[key]) for key in tmp_dict])
            print("-"*15)
        visited.add(tuple(tmp_dict.keys()))
        previous[tuple(tmp_dict.keys())] = {"steps": steps, "dict": deepcopy(tmp_dict)}
        plots2 = tmp_dict

    print("p2", p2, f"took {time.time() - time1}")


# solve_p1()
solve_p2()
