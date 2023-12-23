import sys
from collections import defaultdict
from pprint import pprint


def get_possible(lines):
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def get_neighbours(x, y):
        neighbours = []
        for xx, yy in XY:
            new_x, new_y = x + xx, y + yy
            if (
                0 <= new_x < len(lines[0])
                and 0 <= new_y < len(lines)
                and lines[new_y][new_x] != "#"
            ):
                neighbours.append((new_x, new_y))
        return neighbours

    pos = defaultdict(list)
    # key : [(x, y, distance)]

    start = (1, 0, (1, 0), (-1, -1), 0)
    visited = set()
    Q = [start]
    while Q:
        x, y, start, prev, distance = Q.pop()
        neighbours = [i for i in get_neighbours(x, y) if i != prev]
        if len(neighbours) == 1:
            if (x, y) in visited:
                continue
            visited.add((x, y))
            new_x, new_y = neighbours[0]
            Q.append((new_x, new_y, start, (x, y), distance + 1))
        else:
            pos[start].append((x, y, distance))
            pos[(x, y)].append((*start, distance))
            for neighbour in neighbours:
                new_x, new_y = neighbour
                Q.append((new_x, new_y, (x, y), (x, y), 1))

    return pos


def solve_p2(lines):
    needle = len(lines[0]) - 2, len(lines) - 1
    p2 = 0
    POSSIBLE = get_possible(lines)
    visited = {}

    def dfs(x, y, steps):
        nonlocal p2
        if (x, y) in visited and visited[(x, y)]:
            return
        if (x, y) == needle:
            p2 = max(steps, p2)
        visited[(x, y)] = True
        for new_x, new_y, distance in POSSIBLE[(x, y)]:
            dfs(new_x, new_y, steps + distance)
        visited[(x, y)] = False

    dfs(1, 0, 0)

    print("p2", p2)


def solve_p1(lines):
    source = 1, 0, 0, set()
    x_max, y_max = len(lines[0]), len(lines)
    needle = len(lines[0]) - 2, len(lines) - 1
    stack = [source]
    p1 = set()
    XY = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while stack:
        x, y, steps, visited = stack.pop()
        if (x, y) == needle:
            p1.add(steps)
        for xx, yy in XY:
            X, Y = x + xx, y + yy
            if 0 <= X < x_max and 0 <= Y < y_max:
                if lines[Y][X] == "#":
                    continue
                if lines[Y][X] == ">" and (xx, yy) != (1, 0):
                    continue
                if lines[Y][X] == "v" and (xx, yy) != (0, 1):
                    continue
                if (X, Y) in visited:
                    continue
                visited_cpy = visited.copy()
                visited_cpy.add((x, y))
                stack.append((X, Y, steps + 1, visited_cpy))

    print("p1", max(p1))


lines = open(sys.argv[1]).read().strip().split("\n")
solve_p1(lines)
solve_p2(lines)
