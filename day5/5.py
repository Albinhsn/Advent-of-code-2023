import sys
from collections import deque

lines = open("input").read().split("\n\n")
lines[-1] = lines[-1][:-1]

START = "seed"


def parse(lines):
    m = {}
    for line in lines:
        line = line.split("\n")
        fst, _, snd = line[0].split("-")
        snd = snd.split()[0]
        m[fst] = {
            "ranges": [[int(i) for i in j.split()] for j in line[1:]],
            "to": snd,
            "from": fst,
        }
    return m


def solve_p1():
    def within_range(values, dest):
        for val in values:
            if val[1] <= dest <= val[1] + val[2]:
                return val[0] + dest - val[1]
        return False

    seeds = [int(i) for i in lines[0].split(":")[1].split()]
    map = parse(lines[1:])
    p1 = sys.maxsize
    for seed in seeds:
        ranges = map[START]
        dest = seed
        while True:
            if new_dest := within_range(ranges["ranges"], dest):
                dest = new_dest

            if ranges["to"] == "location":
                break
            ranges = map[ranges["to"]]
        p1 = min(dest, p1)
    print(f"p1:{p1}")


def calc_new_ranges(values, p2_seeds):
    new_seeds = []
    Q = deque(p2_seeds)
    seed_range = Q.popleft()
    while True:
        flag = False
        seed_lower, seed_upper = seed_range[0], seed_range[1]
        for val in values:
            source_lower, source_higher = val[1], val[1] + val[2]

            if seed_lower > source_higher or seed_upper < source_lower:
                continue
            # Our overlapping range
            start = val[0] + max(seed_lower, source_lower) - source_lower
            end = val[0] + min(seed_upper, source_higher) - source_lower
            new_seeds.append((start, end))

            # seed range was within the source range
            if seed_lower >= source_lower and seed_upper <= source_higher:
                flag = True
                break

            # source range was within the seed range
            if seed_lower < source_lower and seed_upper < source_higher:
                Q.append((seed_lower, source_lower - 1))
                seed_range = (source_higher + 1, seed_upper)
                continue

            # we are below with the overlap
            elif seed_lower < source_lower:
                seed_range = (seed_lower, source_lower - 1)

            # we are above with the overlap
            else:
                seed_range = (source_higher + 1, seed_lower)
        if not flag:
            new_seeds.append(seed_range)
        if not Q:
            break
        seed_range = Q.popleft()

    return new_seeds


def solve_p2():
    seeds = [int(i) for i in lines[0].split(":")[1].split()]
    map = parse(lines[1:])
    p2_seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    ranges = map[START]
    while True:
        p2_seeds = calc_new_ranges(ranges["ranges"], p2_seeds)
        if ranges["to"] == "location":
            break
        ranges = map[ranges["to"]]
    print(f"p2:{min([i[0] for i in p2_seeds])}")


solve_p1()
solve_p2()
