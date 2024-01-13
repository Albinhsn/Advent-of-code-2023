import sys
import time
from collections import deque
from copy import deepcopy


def find_place(arr, min_val, max_val):
    for idx, xy in enumerate(arr):
        if xy[0] > max_val:
            arr.insert(idx, (min_val, max_val))
            return arr
        elif xy[1] >= min_val:
            if idx + 1 != len(arr) and arr[idx + 1][0] < max_val:
                i = idx + 1
                while i < len(arr) - 1 and arr[i][0] < max_val:
                    i += 1
                arr = arr[:idx] + [(xy[0], max(max_val, arr[i][1]))] + arr[i + 1 :]
            else:
                arr[idx] = (min(xy[0], min_val), max(xy[1], max_val))
            return arr
    arr.append((min_val, max_val))
    return arr


def print_map(visitedX, visitedY):
    for y in range(min(list(visitedY.keys())), max(list(visitedY.keys())) + 1):
        for x in range(min(list(visitedX.keys())), max(list(visitedX.keys())) + 1):
            if y in visitedY.keys() and len(
                [i for i in visitedY[y] if i[0] <= x <= i[1]]
            ):
                print("#", end="")
            else:
                print(".", end="")
        print()


def solve_p2():
    def walk(pos, steps, dir, visitedX, visitedY):
        x, y = pos
        if dir == "D":
            if x in visitedX:
                visitedX[x] = find_place(visitedX[x], y, y + steps)
            else:
                visitedX[x] = [(y, y + steps)]

            return (x, y + steps)
        if dir == "L":
            if y in visitedY:
                visitedY[y] = find_place(visitedY[y], x - steps, x)
            else:
                visitedY[y] = [(x - steps, x)]

            return (x - steps, y)
        if dir == "R":
            if y in visitedY:
                visitedY[y] = find_place(visitedY[y], x, x + steps)
            else:
                visitedY[y] = [(x, x + steps)]

            return (x + steps, y)
        if dir == "U":
            if x in visitedX:
                visitedX[x] = find_place(visitedX[x], y - steps, y)
            else:
                visitedX[x] = [(y - steps, y)]

            return (x, y - steps)
        raise Exception("How?")

    def check_me(value, lines):
        return len([i for i in lines if i[0] <= value <= i[1]]) > 0

    def is_within(y, x, ylines, xlines):
        above = [i[1] for i in ylines.items() if i[0] < y]
        below = [i[1] for i in ylines.items() if i[0] > y]
        la, lb = 0, 0
        # Need to correct for there is a xline above/below make that line count as 1
        for line in below:
            for b in line:
                if b[0] <= x <= b[1]:
                    lb += 1
        for line in above:
            for b in line:
                if b[0] <= x <= b[1]:
                    la += 1
        if not la or not lb:
            return False
        return la % 2 == 1 or lb % 2 == 1

    lines = open(sys.argv[1]).read().strip().split("\n")
    pos = (0, 0)
    visitedX, visitedY = {}, {}

    # M = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in lines:
        dir, steps, hexa = line.split(" ")
        # dir = M[hexa[-2]]
        # steps = int(hexa[2:-2], 16)

        pos = walk(pos, int(steps), dir, visitedX, visitedY)
    previous =deepcopy(visitedY)
    for xkey, xline in sorted(visitedX.items()):
        for start, stop in xline:
            for i in range(start, stop + 1):
                # Are we within the walls?
                if not is_within(i, xkey + 1, previous, visitedX):
                    continue

                next_wall = [
                    key
                    for (key, val) in sorted(visitedX.items())
                    if check_me(i, val) and key > xkey
                ]
                if next_wall:
                    if i in visitedY:
                        visitedY[i] = find_place(visitedY[i], xkey, next_wall[0])
                    else:
                        visitedY[i] = [(xkey, next_wall[0])]

    print_map(visitedX, visitedY)
    print("-" * 15)
    # time.sleep(0.5)
    answer = 0
    for line in visitedY.values():
        answer += sum([i[1] - i[0] + 1 for i in line])

    print("p2", answer)


def solve_p1():
    def walk(pos, steps, dir):
        if dir == "D":
            return (pos[0], pos[1] + steps), [
                (pos[0], pos[1] + i) for i in range(steps)
            ]
        if dir == "L":
            return (pos[0] - steps, pos[1]), [
                (pos[0] - i, pos[1]) for i in range(steps)
            ]
        if dir == "R":
            return (pos[0] + steps, pos[1]), [
                (pos[0] + i, pos[1]) for i in range(steps)
            ]
        if dir == "U":
            return (pos[0], pos[1] - steps), [
                (pos[0], pos[1] - i) for i in range(steps)
            ]
        raise Exception("How?")

    lines = open(sys.argv[1]).read().strip().split("\n")
    pos = (0, 0)
    visited = set()
    for line in lines:
        dir, steps, _ = line.split(" ")
        pos, new_steps = walk(pos, int(steps), dir)
        visited.update(set(new_steps))

    X = [i[0] for i in visited]
    Y = [i[1] for i in visited]

    x, max_x = min(X) - 1, max(X)
    y = min(Y) + 1

    flag = False
    while True:
        if (x, y) not in visited and flag:
            break
        if (x, y) in visited:
            flag = True
        x += 1
        if x >= max_x:
            x = 0
            y += 1
        if y >= max(Y):
            raise Exception("Ohuh")

    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    Q = deque([(x, y)])
    while Q:
        x, y = Q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for xx, yy in XY:
            if (x + xx, y + yy) not in visited:
                Q.appendleft((x + xx, y + yy))

    print("p1", len(visited))


solve_p1()
solve_p2()
