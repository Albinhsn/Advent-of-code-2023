import sys
from collections import defaultdict
from functools import reduce

seq = open(sys.argv[1]).read()[:-1].split(",")


def hash_me(s):
    return reduce(lambda a, b: ((a + b) * 17), [0] + [ord(char) for char in s]) % 256


def solve_p1(seq):
    print("p1", sum([hash_me(i) for i in seq]))


def solve_p2(seq):
    d = defaultdict(dict)
    for s in seq:
        label = s.split("=")[0] if "=" in s else s.split("-")[0]
        h = hash_me(label)
        if s[-1] == "-":
            if h in d and label in d[h]:
                del d[h][label]
        else:
            focal_length = int(s[-1])
            d[h][label] = focal_length

    answer = 0
    for key, val in d.items():
        for idx, (k2, v2) in enumerate(val.items()):
            answer += (key + 1) * (idx + 1) * v2
    print("p2", answer)


solve_p1(seq)
solve_p2(seq)
