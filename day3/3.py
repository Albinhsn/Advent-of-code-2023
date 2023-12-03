lines = open("./input").read().split("\n")[:-1]

XY = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def solve_p1():
    visited = []
    p1 = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.isdigit() and char != ".":
                for xy in XY:
                    x = j + xy[0]
                    y = i + xy[1]
                    if (
                        x >= len(line)
                        or x < 0
                        or y >= len(lines)
                        or y < 0
                        or not lines[y][x].isdigit()
                    ):
                        continue

                    start = x
                    end = x
                    curr_line = lines[y]
                    while start >= 0 and curr_line[start].isdigit():
                        start -= 1

                    while end < len(curr_line) and curr_line[end].isdigit():
                        end += 1

                    if (start, y) in visited:
                        continue

                    visited.append((start, y))
                    digit = int(curr_line[start + 1 : end])
                    p1 += digit
    print(f"p1:{p1}")


def solve_p2():
    p2 = 0
    visited = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "*":
                found = False
                nmbr = 0
                for xy in XY:
                    x = j + xy[0]
                    y = i + xy[1]
                    if (
                        x >= len(line)
                        or x < 0
                        or y >= len(lines)
                        or y < 0
                        or not lines[y][x].isdigit()
                    ):
                        continue

                    start = x
                    end = x
                    curr_line = lines[y]
                    while start >= 0 and curr_line[start].isdigit():
                        start -= 1

                    while end < len(curr_line) and curr_line[end].isdigit():
                        end += 1

                    if (start, y) in visited:
                        continue

                    visited.append((start, y))
                    if found:
                        p2 += int(curr_line[start + 1 : end]) * nmbr
                    else:
                        nmbr = int(curr_line[start + 1 : end])
                        found = True
    print(f"p2:{p2}")


solve_p1()
solve_p2()
