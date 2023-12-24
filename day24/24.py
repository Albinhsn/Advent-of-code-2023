import sys

import numpy as np


def solve_p1():
    LOW = 200000000000000 if sys.argv[1] == "input" else 7
    HIGH = 400000000000000 if sys.argv[1] == "input" else 27
    lines = open(sys.argv[1]).read().strip().split("\n")
    vectors = []
    for line in lines:
        p, v = line.split("@")
        px, py, pz = map(int, p.split(","))
        vx, vy, vz = map(int, v.split(","))
        vectors.append((px, py, pz, vx, vy, vz))
    p1 = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            px1, py1, pz1, vx1, vy1, vz1 = vectors[i]
            px2, py2, pz2, vx2, vy2, vz2 = vectors[j]

            fst = np.array([[vx1, -vx2], [vy1, -vy2]])
            snd = np.array([px2 - px1, py2 - py1])
            try:
                answer = np.linalg.solve(fst, snd)
            except np.linalg.LinAlgError:
                continue
            x, y = answer

            if (
                LOW <= px1 + x * vx1 <= HIGH
                and LOW <= py1 + x * vy1 <= HIGH
                and x >= 0
                and y >= 0
            ):
                p1 += 1
    print(p1)
