import heapq
import sys


def solve_p1():
    lines = open(sys.argv[1]).read().split("\n")[:-1]
    start = (0, 0)
    needle = (len(lines[0]) - 1, len(lines) - 1)
    # (cost, pos, direction, steps)
    node = (0, start, -1, 0)
    Q = [node]

    visited = set()

    XY = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    MAX_STEPS = 3
    answers = []
    while Q:
        cost, pos, direction, steps = heapq.heappop(Q)

        if (pos, steps, direction) in visited:
            continue

        if pos == needle:
            answers.append(cost)

        visited.add((pos, steps, direction))
        for idx, xy in enumerate(XY):
            x = pos[0] + xy[0]
            y = pos[1] + xy[1]
            s = 1 if idx != direction else 1 + steps

            not_reverse = (idx + 2) % 4 != direction
            inbounds = 0 <= x < len(lines[0]) and 0 <= y < len(lines)
            valid_steps = s <= MAX_STEPS

            if inbounds and not_reverse and valid_steps:
                new_node = (cost + int(lines[y][x]), (x, y), idx, s)
                heapq.heappush(Q, new_node)

    print("p1", min(answers))


def solve_p2():
    lines = open(sys.argv[1]).read().split("\n")[:-1]
    start = (0, 0)
    needle = (len(lines[0]) - 1, len(lines) - 1)
    # (cost, pos, direction, steps)
    node = (0, start, -1, 0)
    Q = [node]

    visited = set()

    XY = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    MAX_STEPS = 10
    answers = []
    while Q:
        cost, pos, direction, steps = heapq.heappop(Q)

        if (pos, steps, direction) in visited:
            continue

        if pos == needle:
            answers.append(cost)

        visited.add((pos, steps, direction))
        for idx, xy in enumerate(XY):
            x = pos[0] + xy[0]
            y = pos[1] + xy[1]
            s = 1 if idx != direction else 1 + steps

            not_reverse = (idx + 2) % 4 != direction

            inbounds = 0 <= x < len(lines[0]) and 0 <= y < len(lines)
            valid_steps = steps <= MAX_STEPS and (steps >= 4 or direction in [idx, -1])

            if inbounds and not_reverse and valid_steps:
                new_node = (cost + int(lines[y][x]), (x, y), idx, s)
                heapq.heappush(Q, new_node)
    print("p2", min(answers))


solve_p1()
solve_p2()
