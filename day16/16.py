import sys
from collections import deque


def solve(pos, dir, lines):
    visited = []

    Q = deque([(pos, dir)])
    while Q:
        curr = Q.popleft()

        # check if out of bounds
        if curr in visited:
            continue

        pos, direction = curr
        if pos[1] < 0 or pos[1] >= len(lines) or pos[0] < 0 or pos[0] >= len(lines[0]):
            continue

        visited.append(curr)

        tile = lines[pos[1]][pos[0]]
        match tile:
            case ".":
                pos = pos[0] + direction[0], pos[1] + direction[1]
                Q.append((pos, direction))
                continue
            case "|":
                if direction == (1, 0) or direction == (-1, 0):
                    Q.extend(
                        [
                            ((pos[0], pos[1] + 1), (0, 1)),
                            ((pos[0], pos[1] - 1), (0, -1)),
                        ]
                    )
                else:
                    Q.append(
                        (
                            (pos[0] + direction[0], pos[1] + direction[1]),
                            direction,
                        )
                    )
            case "-":
                if direction == (0, 1) or direction == (0, -1):
                    Q.extend(
                        [
                            ((pos[0] + 1, pos[1]), (1, 0)),
                            ((pos[0] - 1, pos[1]), (-1, 0)),
                        ]
                    )
                else:
                    pos = pos[0] + direction[0], pos[1] + direction[1]
                    Q.append((pos, direction))
            case "\\":
                if direction == (0, 1):
                    pos = pos[0] + 1, pos[1]
                    Q.append((pos, (+1, 0)))

                elif direction == (0, -1):
                    pos = pos[0] - 1, pos[1]
                    Q.append((pos, (-1, 0)))

                elif direction == (1, 0):
                    pos = pos[0], pos[1] + 1
                    Q.append((pos, (0, 1)))

                # direction = (-1, 0)
                else:
                    pos = pos[0], pos[1] - 1
                    Q.append((pos, (0, -1)))
            case "/":
                if direction == (0, 1):
                    pos = pos[0] - 1, pos[1]
                    Q.append((pos, (-1, 0)))

                elif direction == (0, -1):
                    pos = pos[0] + 1, pos[1]
                    Q.append((pos, (1, 0)))

                elif direction == (1, 0):
                    pos = pos[0], pos[1] - 1
                    Q.append((pos, (0, -1)))

                # direction = (-1, 0)
                else:
                    pos = pos[0], pos[1] + 1
                    Q.append((pos, (0, 1)))
    tiles = [i[0] for i in visited]
    return len(set(tiles))


def solve_p1():
    lines = open(sys.argv[1]).read().split("\n")[:-1]
    answer = solve((0, 0), (1, 0), lines)
    print("p1", answer)


def solve_p2():
    lines = open(sys.argv[1]).read().split("\n")[:-1]
    answer = 0
    for Y in range(len(lines)):
        pos1 = (0, Y)
        pos2 = (len(lines[0]) - 1, Y)
        answer = max(answer, solve(pos1, (1, 0), lines), solve(pos2, (-1, 0), lines))
        print(f"Y: {100*(Y+1)/len(lines)}")

    for X in range(len(lines)):
        pos1 = (X, 0)
        pos2 = (X, len(lines) - 1)
        answer = max(answer, solve(pos1, (0, 1), lines), solve(pos2, (0, -1), lines))
        print(f"X: {100*(X+1)/len(lines[0])}")
    print("p2", answer)


solve_p1()
solve_p2()
