from collections import deque

lines = open("input").read().split("\n")[:-1]


def get_neighbours(pos):
    char = lines[pos[1]][pos[0]]
    x, y = pos
    return {
        "|": [(x, y - 1), (x, y + 1)],
        "-": [(x + 1, y), (x - 1, y)],
        "L": [(x, y - 1), (x + 1, y)],
        "J": [(x, y - 1), (x - 1, y)],
        "7": [(x, y + 1), (x - 1, y)],
        "F": [(x, y + 1), (x + 1, y)],
        ".": [],
        "S": [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)],
    }[char]


def get_first_pipe(pos):
    neighbours = [n for n in get_neighbours(pos) if not not_valid_pos(n)]
    neigh_neigh = [(get_neighbours(n), n) for n in neighbours]
    return [n[1] for n in neigh_neigh if pos in n[0]][0]


def not_valid_pos(pos):
    x, y = pos
    if x < 0 or x >= len(lines[0]):
        return True
    if y < 0 or y >= len(lines):
        return True

    return False


def traverse(needle):
    pos = get_first_pipe(needle)
    prev_pos = needle
    path = [prev_pos]

    while True:
        if path and pos == needle:
            return path

        path.append(pos)
        fst, snd = get_neighbours(pos)
        tmp = pos
        pos = fst if fst != prev_pos else snd
        prev_pos = tmp


def get_start_pos(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)


def print_map_p2(path, p2):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) in path:
                print(lines[y][x], end="")
            elif (x, y) in p2:
                print("I", end="")
            else:
                print(".", end="")
        print()


def print_map():
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) != (8, 5):
                print(lines[y][x], end="")
            else:
                print("A", end="")
        print()


def get_minmax(path):
    x = [p[0] for p in path]
    y = [p[1] for p in path]
    return min(x), max(x), min(y), max(y)


def get_c(x, y):
    assert x == int(x) and y == int(y), f"Sent floats?  {x,y}"
    return lines[int(y)][int(x)]


def get_escape_path(curr):
    Q = deque([])
    if curr[0] == int(curr[0]) and curr[1] == int(curr[1]):
        XY = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for x, y in XY:
            if int(curr[1] + y) < 0 or int(curr[1] + y) >= len(lines):
                continue
            if int(curr[0] + x) < 0 or int(curr[0] + x) >= len(lines[0]):
                continue
            if lines[int(curr[1] + y)][int(curr[0] + x)] == ".":
                Q.append((curr[0] + x, curr[1] + y))
        # check left
        if (
            get_c(curr[0] - 1, curr[1] + 1) == "."
            or get_c(curr[0] - 1, curr[1] - 1) == "."
            or get_c(curr[0] - 1, curr[1]) == "."
        ):
            ...
        elif get_c(curr[0] - 1, curr[1] - 1) not in ["7", "F", "|", "S"]:
            Q.append((curr[0] - 1, curr[1] - 0.5))
        elif get_c(curr[0] - 1, curr[1] + 1) not in ["J", "|", "L", "S"]:
            Q.append((curr[0] - 1, curr[1] + 0.5))

        # check right
        if (
            get_c(curr[0] + 1, curr[1] + 1) == "."
            or get_c(curr[0] + 1, curr[1] - 1) == "."
            or get_c(curr[0] + 1, curr[1]) == "."
        ):
            ...
        elif get_c(curr[0] + 1, curr[1] - 1) not in ["7", "|", "F", "S"]:
            Q.append((curr[0] + 1, curr[1] - 0.5))
        elif get_c(curr[0] + 1, curr[1] + 1) not in ["J", "|", "L", "S"]:
            Q.append((curr[0] + 1, curr[1] + 0.5))

        # check up
        if (
            get_c(curr[0] - 1, curr[1] - 1) == "."
            or get_c(curr[0] + 1, curr[1] - 1) == "."
            or get_c(curr[0], curr[1] - 1) == "."
        ):
            ...
        elif get_c(curr[0] - 1, curr[1] - 1) not in ["F", "-", "L", "S"]:
            Q.append((curr[0] - 0.5, curr[1] - 1))
        elif get_c(curr[0] + 1, curr[1] - 1) not in ["7", "-", "J", "S"]:
            Q.append((curr[0] + 0.5, curr[1] - 1))

        # check down
        if (
            get_c(curr[0] - 1, curr[1] + 1) == "."
            or get_c(curr[0] + 1, curr[1] + 1) == "."
            or get_c(curr[0], curr[1] + 1) == "."
        ):
            ...
        elif get_c(curr[0] - 1, curr[1] + 1) not in ["F", "-", "L", "S"]:
            Q.append((curr[0] - 0.5, curr[1] + 1))
        elif get_c(curr[0] + 1, curr[1] + 1) not in ["7", "-", "J", "S"]:
            Q.append((curr[0] + 0.5, curr[1] + 1))

    elif curr[0] != int(curr[0]):
        xl, xr = curr[0] - 0.5, curr[0] + 0.5
        yl, yr = curr[1] + 1, curr[1] - 1
        if get_c(xl, yl) == ".":
            Q.append((xl, yl))
        if get_c(xr, yl) == ".":
            Q.append((xr, yl))
        if get_c(xl, yr) == ".":
            Q.append((xl, yr))
        if get_c(xr, yr) == ".":
            Q.append((xr, yr))

        xlyl = get_c(xl, yl)
        xryl = get_c(xr, yl)

        xlyr = get_c(xl, yr)
        xryr = get_c(xr, yr)
        xl1 = get_c(xl, curr[1])
        xr1 = get_c(xr, curr[1])
        # print("-" * 15)
        # print(curr)
        # print(xlyr, " ", xryr)
        # print(get_c(xl, curr[1]), ".", get_c(xr, curr[1]))
        # print(xlyl, " ", xryl)

        # Check if we can move down
        if (xlyl, xryl) in [
            ("|", "|"),
            ("|", "F"),
            ("|", "L"),
            ("|", "S"),
            ("S", "|"),
            ("S", "F"),
            ("S", "L"),
            ("7", "|"),
            ("7", "S"),
            ("7", "L"),
            ("7", "F"),
            ("J", "|"),
            ("J", "S"),
            ("J", "L"),
            ("J", "F"),
        ]:
            # X, y -1
            # print("Down", xlyl, xryl)
            Q.append((curr[0], yl))
        # check if we can move down and left
        if (xl1, xlyl) in [
            ("J", "-"),
            ("J", "S"),
            ("J", "F"),
            ("J", "7"),
            ("S", "F"),
            ("S", "-"),
            ("S", "7"),
        ]:
            # print("Down left", xl1, xlyl)
            Q.append((xl, curr[1] + 0.5))
        # check if we can move down and right
        if (xr1, xryl) in [("S", "-"), ("L", "-"), ("L", "7"), ("S", "7"), ("L", "F")]:
            # print("Down right", xr1, xryl)
            # x - 0.5 , y + 0.5
            Q.append((xr, curr[1] + 0.5))

        # Check if we can move up
        if (xlyr, xryr) in [
            ("|", "|"),
            ("|", "F"),
            ("|", "L"),
            ("|", "S"),
            ("J", "|"),
            ("J", "L"),
            ("J", "S"),
            ("J", "F"),
            ("7", "F"),
            ("7", "S"),
            ("7", "|"),
            ("7", "L"),
            ("S", "|"),
            ("S", "F"),
            ("S", "L"),
        ]:
            # print("Up", xlyr, xryr)
            Q.append((curr[0], yr))
        # check if we can move up and left
        if (xlyr, xl1) in [("-", "S"), ("L", "S"), ("L", "7"), ("-", "7"), ("J", "7")]:
            # print("Up left", xlyr, xryr)
            Q.append((xl, curr[1] - 0.5))
        elif (xlyr, xryr) == ("S", "7") and get_c(xl, yr + 1) not in ["|", "J", "L"]:
            # print("Up left", xlyr, xryr)
            Q.append((xl, curr[1] - 0.5))

        # check if we can move up and right
        # SWAPPED VARS
        if (xr1, xryr) in [
            ("S", "-"),
            ("S", "J"),
            ("F", "-"),
            ("F", "J"),
            ("F", "S"),
            ("F", "L"),
        ]:
            # print("Up right", xr1, xryr)
            Q.append((xr, curr[1] - 0.5))

    else:
        xl, xr = curr[0] - 1, curr[0] + 1
        yl, yr = curr[1] + 0.5, curr[1] - 0.5
        if get_c(xl, yl) == ".":
            Q.append((xl, yl))
        if get_c(xr, yl) == ".":
            Q.append((xr, yl))
        if get_c(xl, yr) == ".":
            Q.append((xl, yr))
        if get_c(xr, yr) == ".":
            Q.append((xr, yr))

        xlyl = get_c(xl, yl)
        xryl = get_c(xr, yl)

        xlyr = get_c(xl, yr)
        xryr = get_c(xr, yr)
        yr0 = get_c(curr[0], yr)
        yl0 = get_c(curr[0], yl)
        # print("-" * 15)
        # print(curr)
        # print(xlyr, "", get_c(curr[0], yr), "", xryr)
        # print("   .")
        # print(xlyl, "", get_c(curr[0], yl), "", xryl)

        # Check if we can move left
        if xlyl not in [".", "L", "J", "S", "|"] and xlyr != ".":
            # print("Left", xlyl, xlyr)
            Q.append((xl, curr[1]))
        # Check if we can move left and up
        if (xlyr, yr0) in [
            ("7", "S"),
            ("7", "L"),
            ("S", "L"),
            ("J", "L"),
            ("|", "L"),
            ("|", "S"),
        ]:
            # print("Left up", xlyr, yr0)
            Q.append((curr[0] - 0.5, yr))
        # Check if we can move left and down
        if (xlyl, yl0) in [
            ("S", "J"),
            ("F", "J"),
            ("F", "|"),
            ("J", "F"),
            ("|", "F"),
            ("7", "F"),
            ("7", "S"),
        ]:
            # print("Left down", xlyl, yl0)
            Q.append((curr[0] - 0.5, yl))

        # Check if we can move right
        if xryl not in ["L", ".", "J", "S", "|"] and xryr != ".":
            # print("Right", xryl, xryr)
            Q.append((xr, curr[1]))
        # Check if we can move right and up
        if (yr0, xryr) in [
            ("S", "F"),
            ("J", "|"),
            ("J", "S"),
            ("J", "F"),
            ("S", "|"),
            ("S", "L"),
            ("J", "L"),
        ]:
            # print("Right up", yr0, xryr)
            # elif xryl in ["S", "J"] and xryr in ["|", "S", "F", "J"]:
            Q.append((curr[0] + 0.5, yr))
        # Check if we can move right and down
        if (yl0, xryl) in [
            ("S", "L"),
            ("S", "F"),
            ("S", "|"),
            ("7", "|"),
            ("7", "S"),
            ("7", "L"),
            ("7", "F"),
        ]:
            # print("Right down", yl0, xryl)
            # elif xryr in ["S", "7"] and xryl in ["|", "S", "L"]:
            Q.append((curr[0] + 0.5, yl))

    return Q


def not_within_range(curr, min_x, max_x, min_y, max_y):
    return curr[0] <= min_x or curr[0] >= max_x or curr[1] <= min_y or curr[1] >= max_y


def escape(min_x, max_x, min_y, max_y, pos):
    Q = deque([pos])
    visited = []
    while Q:
        curr = Q.popleft()
        if curr in visited:
            continue
        if not_within_range(curr, min_x, max_x, min_y, max_y):
            return []

        visited.append(curr)
        q = get_escape_path(curr)
        if [
            i
            for i in q
            if not not_within_range(i, min_x, max_x, min_y, max_y)
            and curr not in get_escape_path(i)
        ]:
            missing = [
                i
                for i in q
                if not not_within_range(i, min_x, max_x, min_y, max_y)
                and curr not in get_escape_path(i)
            ]
            raise Exception(f"{curr} -> {missing[0]}")

        Q.extendleft(q)

    return [v for v in visited if v[0] == int(v[0]) and v[1] == int(v[1])]


def solve_p2(path):
    min_x, max_x, min_y, max_y = get_minmax(path)
    count = 0
    visited = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in visited:
                continue
            if lines[y][x] == ".":
                loc_visited = escape(min_x, max_x, min_y, max_y, (x, y))
                count += len(loc_visited)
                visited.extend(loc_visited)
    print_map_p2(path, visited)
    return visited


def change_lines(path):
    global lines
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) not in path:
                lines[y] = lines[y][:x] + "." + lines[y][x + 1 :]


start_pos = get_start_pos(lines)
path = traverse(start_pos)
print("p1", len(path) // 2)

change_lines(path)
# print_map()

p2 = solve_p2(path)
print(len(p2))
# print(get_escape_path((2, 1.5)))
# print_map_p2(path, p2)
# print("p2", len(p2))
