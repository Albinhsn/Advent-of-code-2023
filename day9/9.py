def solve_p1(line):
    lines = [line]
    last = line
    while sum(last) != 0:
        last = [last[i + 1] - last[i] for i in range(len(last) - 1)]
        lines.append(last)
    curr = 0
    for i in range(1, len(lines)):
        curr += lines[-1 - i][-1]
    return curr


def solve_p2(line):
    lines = [line]
    last = line
    while sum(last) != 0:
        last = [last[i + 1] - last[i] for i in range(len(last) - 1)]
        lines.append(last)
    curr = 0
    for i in range(1, len(lines)):
        curr = lines[-1 - i][0] - curr

    return curr


lines = [list(map(int, x.split())) for x in open("input").read().split("\n")[:-1]]
print("p1", sum([solve_p1(line) for line in lines]))
print("p2", sum([solve_p2(line) for line in lines]))
