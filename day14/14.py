import sys
from copy import deepcopy


def nw(lines):
    for line in lines:
        i = 0
        wall = -1
        while i < len(line):
            if line[i] == 1:
                line[i] = 0
                wall += 1
                line[wall] = 1
            elif line[i] == 2:
                wall = i
            i += 1


def se(lines):
    for line in lines:
        i = len(line) - 1
        wall = len(line)
        while i >= 0:
            if line[i] == 1:
                line[i] = 0
                wall -= 1
                line[wall] = 1
            elif line[i] == 2:
                wall = i
            i -= 1


def rotate(lines):
    return [[lines[i][j] for i in range(len(lines))] for j in range(len(lines[0]))]


def solve_p1(lines):
    lines = deepcopy(lines)
    lines = rotate(lines)
    nw(lines)
    lines = rotate(lines)
    print(
        "p1",
        sum(
            [
                (len(lines) - idx) * len([i for i in line if i == 1])
                for idx, line in enumerate(lines)
            ]
        ),
    )


def solve_p2(lines):
    lines = deepcopy(lines)
    CYCLES = 1_000_000_000
    i = 0
    visited = {}
    while i < CYCLES:
        t = tuple([tuple(i) for i in lines])
        if t in visited:
            cycle_length = i - visited[t]
            CYCLES = (CYCLES - i) % cycle_length
            i = 0
            visited = {}
            continue
        visited[t] = i
        lines = rotate(lines)
        nw(lines)
        lines = rotate(lines)
        nw(lines)
        lines = rotate(lines)
        se(lines)
        lines = rotate(lines)
        se(lines)
        i += 1
    print(
        "p2",
        sum(
            [
                (len(lines) - idx) * len([i for i in line if i == 1])
                for idx, line in enumerate(lines)
            ]
        ),
    )


m = {".": 0, "O": 1, "#": 2}
lines = [[m[i] for i in line] for line in open(sys.argv[1]).read().split("\n")[:-1]]
solve_p1(lines)
solve_p2(lines)
