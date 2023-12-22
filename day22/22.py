import sys
from collections import deque

sys.setrecursionlimit(1500)

DEBUG = True


def parse(line):
    return tuple(tuple(map(int, i.split(","))) for i in line.split("~"))


def get_char(x):
    return chr(ord("A") + x)


def get_idx(x):
    return ord(x) - ord("A")


def print_xz(lines):
    min_x, max_x = min(min(i[0][0], i[1][0]) for i in lines), max(
        max(i[0][0], i[1][0]) for i in lines
    )
    min_z, max_z = min(min(i[0][2], i[1][2]) for i in lines), max(
        max(i[0][2], i[1][2]) for i in lines
    )
    print(f"X: {min_x}, {max_x}")
    print(f"Z: {min_z}, {max_z}")
    for z in reversed(range(min_z, max_z + 1)):
        for x in range(min_x, max_x + 1):
            # Check if x and z in within the range of values of a line
            flag = False
            for idx, line in enumerate(lines):
                if line[0][0] <= x <= line[1][0] and line[0][2] <= z <= line[1][2]:
                    print(get_char(idx), end="")
                    flag = True
                    break
            if not flag:
                print(".", end="")
        print()


def print_yz(lines):
    min_y, max_y = min(min(i[0][1], i[1][1]) for i in lines), max(
        max(i[0][1], i[1][1]) for i in lines
    )
    min_z, max_z = min(min(i[0][2], i[1][2]) for i in lines), max(
        max(i[0][2], i[1][2]) for i in lines
    )
    print(f"Y: {min_y}, {max_y}")
    print(f"Z: {min_z}, {max_z}")
    for z in reversed(range(min_z, max_z + 1)):
        for y in range(min_y, max_y + 1):
            # Check if x and z in within the range of values of a line
            flag = False
            for idx, line in enumerate(lines):
                if line[0][1] <= y <= line[1][1] and line[0][2] <= z <= line[1][2]:
                    print(get_char(idx), end="")
                    flag = True
                    break
            if not flag:
                print(".", end="")
        print()


def print_fallen_yz(lines, H):
    min_y, max_y = min(min(i[0][1], i[1][1]) for i in lines), max(
        max(i[0][1], i[1][1]) for i in lines
    )
    min_z, max_z = min(H.values()), max(H.values())
    print(f"Y: {min_y}, {max_y}")
    print(f"Z: {min_z}, {max_z}")
    for z in reversed(range(min_z, max_z + 1)):
        for y in range(min_y, max_y + 1):
            # Check if x and z in within the range of values of a line
            flag = False
            fst, snd = None, None
            for idx, line in enumerate(lines):
                if (
                    line[0][1] <= y <= line[1][1]
                    and H[get_char(idx)] - line[1][2] + line[0][2]
                    <= z
                    <= H[get_char(idx)]
                ):
                    if not fst:
                        fst = get_char(idx)
                    else:
                        snd = get_char(idx)
                        break
                    flag = True
            if fst and snd:
                print("?", end="")
            elif fst:
                print(fst, end="")
            elif not flag:
                print(".", end="")
        print()


def print_fallen_xz(lines, H):
    min_x, max_x = min(min(i[0][0], i[1][0]) for i in lines), max(
        max(i[0][0], i[1][0]) for i in lines
    )
    min_z, max_z = min(H.values()), max(H.values())
    print(f"X: {min_x}, {max_x}")
    print(f"Z: {min_z}, {max_z}")
    for z in reversed(range(min_z, max_z + 1)):
        for x in range(min_x, max_x + 1):
            # Check if x and z in within the range of values of a line
            flag = False
            fst, snd = None, None
            for idx, line in enumerate(lines):
                if (
                    line[0][0] <= x <= line[1][0]
                    and H[get_char(idx)] - line[1][2] + line[0][2]
                    <= z
                    <= H[get_char(idx)]
                ):
                    if not fst:
                        fst = get_char(idx)
                    else:
                        snd = get_char(idx)
                        break
                    flag = True
            if fst and snd:
                print("?", end="")
            elif fst:
                print(fst, end="")
            elif not flag:
                print(".", end="")
        print()


def change_val(val, lines):
    above, below = val
    if DEBUG:
        above = set(get_char(lines.index(v)) for v in above)
        below = set(get_char(lines.index(b)) for b in below)
    else:
        above = set(lines.index(v) for v in above)
        below = set(lines.index(b) for b in below)
    return above, below


def calc_heights_iter(lines, M, heights):
    Q = deque([])
    for key, (_, below) in M.items():
        line = lines[get_idx(key)]
        height = line[1][2] - line[0][2] + 1
        if not below:
            heights[key] = height
            continue
        Q.append((key, below, height))
    while Q:
        key, below, height = Q.popleft()
        if len([i for i in below if i in heights]) == len(below):
            heights[key] = height + max(h for h in [heights[k] for k in below])
            continue
        Q.append((key, below, height))


def solve_p2(lines):
    M, _, above, below = get_transforms(lines)
    p2 = 0
    for key in M:
        fallen = set()
        visited = set()
        Q = deque([key])
        while Q:
            curr = Q.popleft()
            for val in above[curr]:
                if val in visited:
                    continue
                if len(below[val]) == 1:
                    p2 += 1
                    Q.append(val)
                    fallen.add(val)
                    visited.add(val)
                elif len([i for i in below[val] if i in fallen]) == len(below[val]):
                    p2 += 1
                    Q.append(val)
                    fallen.add(val)
                    visited.add(val)
    print("p2", p2)


def get_transforms(lines):
    M = {}
    heights = {}
    for idx, line in enumerate(lines):
        above = set()
        below = set()
        for i, l in enumerate(lines):
            if i == idx:
                continue
            if l[0][0] > line[1][0] or line[0][0] > l[1][0]:
                continue
            if l[0][1] > line[1][1] or line[0][1] > l[1][1]:
                continue
            if l[0][2] > line[1][2]:
                above.add(l)
            elif l[1][2] < line[0][2]:
                below.add(l)

        if DEBUG:
            heights[get_char(idx)] = line[1][2] - line[0][2] + 1
            M[get_char(idx)] = (above, below)
        else:
            heights[idx] = line[1][2] - line[0][2] + 1
            M[idx] = (above, below)
    M = {k: change_val(v, lines) for k, v in M.items()}
    H = {}
    calc_heights_iter(lines, M, H)
    supported_by = {
        key: [i for i in above if H[i] == H[key] + heights[i]]
        for (key, (above, _)) in M.items()
    }
    supports = {
        key: [i for i in below if H[i] + heights[key] == H[key]]
        for (key, (_, below)) in M.items()
    }
    return M, H, supported_by, supports


def solve_p1(lines):
    _, _, supported_by, supports = get_transforms(lines)
    answer = 0
    for val in supported_by.values():
        if not val:
            answer += 1
            continue
        flag = True
        for va in val:
            if len(supports[va]) == 1:
                flag = False
                break
        if flag:
            answer += 1

    print("p1", answer)


lines = [parse(line) for line in open(sys.argv[1]).read().strip().split("\n")]
solve_p1(lines)
solve_p2(lines)
