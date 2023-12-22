import math
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
    def is_valid(x, y, X, Y, lines):
        x = x - (x // X) * X
        y = y - (y // Y) * Y
        return lines[y][x] != "#"

    time1 = time.time()
    lines = open(sys.argv[1]).read().strip().split("\n")
    x, y = [
        [(idx, i) for idx, x in enumerate(y) if x == "S"][0]
        for i, y in enumerate(lines)
        if "S" in y
    ][0]
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    X, Y = len(lines[0]), len(lines)
    STEPS = 10

    plots1 = set()
    plots2 = set()
    plots2.add((x, y))
    p2 = 1
    for steps in range(STEPS // 2):
        tmp = set()
        for x, y in plots2:
            tmp.update(
                (x + xx, y + yy)
                for (xx, yy) in XY
                if (x + xx, y + yy) not in plots1
                and is_valid(abs(x + xx), abs(y + yy), X, Y, lines)
            )
        plots1 = tmp
        print(len(plots1))

        tmp = set()
        for x, y in plots1:
            tmp.update(
                (x + xx, y + yy)
                for (xx, yy) in XY
                if (x + xx, y + yy) not in plots2
                and is_valid(abs(x + xx), abs(y + yy), X, Y, lines)
            )
        plots2 = tmp
        print(len(plots2))
        print("-")
        p2 += len(plots2)

    print("p2", p2, f"took {time.time() - time1}")


# solve_p1()
solve_p2()
