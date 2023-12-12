from itertools import combinations


def get_galaxies(lines):
    galaxies = []
    for y, line in enumerate(lines):
        if "#" not in line:
            continue
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))

    return galaxies


lines = open("input").read().split("\n")[:-1]
galaxies = get_galaxies(lines)

j0 = [j[0] for j in galaxies]
j1 = [j[1] for j in galaxies]

EXTRAS = 999_999


def find_path_p1(source, needle):
    MIN0 = min(source[0], needle[0])
    MAX0 = max(source[0], needle[0])
    MIN1 = min(source[1], needle[1])
    MAX1 = max(source[1], needle[1])
    length = MAX0 - MIN0 + MAX1 - MIN1
    length += sum([1 for i in range(MIN0 + 1, MAX0) if i not in j0])
    length += sum([1 for i in range(MIN1 + 1, MAX1) if i not in j1])

    return length


def find_path_p2(source, needle):
    MIN0 = min(source[0], needle[0])
    MAX0 = max(source[0], needle[0])
    MIN1 = min(source[1], needle[1])
    MAX1 = max(source[1], needle[1])
    length = MAX0 - MIN0 + MAX1 - MIN1
    length += sum([EXTRAS for i in range(MIN0 + 1, MAX0) if i not in j0])
    length += sum([EXTRAS for i in range(MIN1 + 1, MAX1) if i not in j1])

    return length


comb = list(combinations(galaxies, 2))
p1 = 0
p2 = 0
done = []

for idx, (source, needle) in enumerate(comb):
    if (needle, source) not in done and source != needle:
        p2 += find_path_p2(source, needle)
        p1 += find_path_p1(source, needle)
        done.append((source, needle))
print("p1", p1)
print("p2", p2)
