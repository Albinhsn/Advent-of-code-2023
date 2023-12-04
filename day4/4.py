from collections import Counter

lines = open("input").read().split("\n")[:-1]


def get_matches(line):
    winning, rest = line.split(":")[1].split("|")
    return len([x for x in rest.split() if x in winning.split()])


def solve_p1(line):
    matches = get_matches(line)
    return 0 if not matches else pow(2, matches - 1)


def solve_p2(lines):
    counter = Counter({i: 1 for i in range(len(lines))})
    for idx, line in enumerate(lines):
        for i in range(idx + 1, idx + get_matches(line) + 1):
            if i >= len(lines):
                break
            counter[i] += counter[idx]

    return sum(counter.values())


print(f"p1: {sum([solve_p1(i) for i in lines])}\np2: {solve_p2(lines)}")
