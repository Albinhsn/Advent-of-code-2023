import sys
import time
from collections import defaultdict, deque


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
    def get_neighbours(x, y):
        neighbours = set()
        for xx, yy in XY:
            grid = (0, 0)
            XX = x + xx
            YY = y + yy
            if XX < 0:
                XX += X
                grid = (-1, 0)
            elif XX >= X:
                XX -= X
                grid = (0, 1)
            if YY < 0:
                YY += Y
                grid = grid[0], -1
            elif YY >= Y:
                YY -= Y
                grid = grid[0], 1
            if lines[YY][XX] == "#":
                continue
            neighbours.add((XX, YY, grid))
        return neighbours

    def print_map(plots):
        for y in range(Y):
            for x in range(X):
                if lines[y][x] == "S":
                    print("S", end="")
                if (x, y) in plots:
                    print("0", end="")
                else:
                    print(lines[y][x], end="")
            print()

    time1 = time.time()
    lines = open(sys.argv[1]).read().strip().split("\n")
    XX, YY = [
        [(idx, i) for idx, x in enumerate(y) if x == "S"][0]
        for i, y in enumerate(lines)
        if "S" in y
    ][0]
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    X, Y = len(lines[0]), len(lines)
    STEPS = 10

    plots1 = defaultdict(set)
    plots2 = defaultdict(set)
    plots2[(XX, YY)].add((0, 0))
    for _ in range(STEPS // 2):
        for (x, y), val in plots2.items():
            for XX, YY, grid in get_neighbours(x, y):
                to_add = (
                    set([g for g in val if g not in plots2[XX, YY]])
                    if grid == (0, 0)
                    else set(
                        (grid[0] + g[0], grid[1] + g[1])
                        for g in val
                        if (grid[0] + g[0], grid[1] + g[1]) not in plots1[XX, YY]
                    )
                )
                if to_add:
                    plots1[XX, YY].update(to_add)
        print(f"plots1 {sum(len(i) for i in plots1.values())}", set(plots1.keys()))
        print_map(plots1)
        for (x, y), val in plots1.items():
            for XX, YY, grid in get_neighbours(x, y):
                to_add = (
                    set(g for g in val if g not in plots2[XX, YY])
                    if grid == (0, 0)
                    else set(
                        (grid[0] + g[0], grid[1] + g[1])
                        for g in val
                        if (grid[0] + g[0], grid[1] + g[1]) not in plots2[XX, YY]
                    )
                )
                if to_add:
                    plots2[XX, YY].update(to_add)
        print(f"plots2 {sum(len(i) for i in plots2.values())}", set(plots2.keys()))
        print_map(plots2)

    print("p2", sum(len(i) for i in plots2.values()), f"took {time.time() - time1}")


# solve_p1()
solve_p2()
