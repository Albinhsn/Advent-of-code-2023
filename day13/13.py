lines = [i.split("\n") for i in open("input").read().split("\n\n")]
lines[-1] = lines[-1][:-1]


def solve_p2(rows) -> int:
    def get_diff(l1, l2):
        return len([j for idx, j in enumerate(l1) if l2[idx] != j]) == 1

    def solve(line):
        i = 0
        while i + 1 < len(line):
            flag, changed = False, False

            if (smudge := get_diff(line[i], line[i + 1])) or line[i] == line[i + 1]:
                if smudge:
                    changed = True
                diff = 1

                while i + diff < len(line) - 1 and i - diff >= 0:
                    dec, inc = line[i - diff], line[i + diff + 1]

                    if get_diff(inc, dec) and not changed:
                        changed = True
                    elif inc != dec:
                        flag = True
                        break

                    diff += 1

                if not flag and changed:
                    return i + 1
            i += 1
        return 0

    if answer := solve(rows):
        return answer * 100

    columns = [
        "".join([rows[i][j] for i in range(len(rows))]) for j in range(len(rows[0]))
    ]
    return solve(columns)


def solve_p1(rows) -> int:
    def solve(line):
        i = 0
        while i + 1 < len(line):
            flag = False
            if line[i] == line[i + 1]:
                diff = 1
                while i + diff + 1 < len(line) and i - diff >= 0:
                    if line[i + diff + 1] != line[i - diff]:
                        flag = True
                        break
                    diff += 1
                if not flag:
                    return i + 1
            i += 1
        return 0

    columns = [
        "".join([rows[i][j] for i in range(len(rows))]) for j in range(len(rows[0]))
    ]
    if answer := solve(columns):
        return answer
    return solve(rows) * 100


print("p1", sum([solve_p1(line) for line in lines]))
print("p2", sum([solve_p2(line) for line in lines]))
