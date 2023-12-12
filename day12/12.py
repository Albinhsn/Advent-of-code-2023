lines = open("input").read().split("\n")[:-1]


def solve_p1(line):
    def solve(springs, record) -> int:
        if not springs or not record:
            if [i for i in springs if "#" in i]:
                return 0
            return 0 if record else 1

        score = 0
        curr, rest = record[0], record[1:]
        for i in range(len(springs)):
            if curr > len(springs[i]):
                if "#" not in springs[i]:
                    score += solve(springs[i + 1 :], record)
                return score
            elif curr == len(springs[i]):
                score += solve(springs[i + 1 :], rest)
            else:
                spring = springs[i]
                for j in range(len(spring) - curr + 1):
                    if curr + j == len(spring):
                        score += solve(springs[i + 1 :], rest)
                        break
                    if spring[curr + j] != "#":
                        springs[i] = spring[j + curr + 1 :]
                        if not springs[i]:
                            score += solve(springs[i + 1 :], rest)
                        else:
                            score += solve(springs[i:], rest)
                        springs[i] = spring
                    if spring[j] == "#":
                        break
            if "#" in springs[i]:
                return score

        return score

    springs, record = line.split()
    record = list(map(int, record.split(",")))
    springs = [i for i in springs.split(".") if len(i) > 0]

    return solve(springs, record)


def solve_p2(line):
    done = {}

    def solve(springs, record) -> int:
        if (".".join(springs), record) in done:
            return done[(".".join(springs), record)]

        if not springs or not record:
            if [i for i in springs if "#" in i]:
                return 0
            return 0 if record else 1

        score = 0
        curr, rest = record[0], record[1:]
        for i in range(len(springs)):
            if curr > len(springs[i]):
                if "#" not in springs[i]:
                    score += solve(springs[i + 1 :], record)
                done[(".".join(springs), record)] = score
                return score
            elif curr == len(springs[i]):
                score += solve(springs[i + 1 :], rest)
            else:
                spring = springs[i]
                for j in range(len(spring) - curr + 1):
                    if curr + j == len(spring):
                        score += solve(springs[i + 1 :], rest)
                        break
                    if spring[curr + j] != "#":
                        springs[i] = spring[j + curr + 1 :]
                        if not springs[i]:
                            score += solve(springs[i + 1 :], rest)
                        else:
                            score += solve(springs[i:], rest)
                        springs[i] = spring
                    if spring[j] == "#":
                        break
            if "#" in springs[i]:
                done[(".".join(springs), record)] = score
                return score

        done[(".".join(springs), record)] = score
        return score

    springs, record = line.split()
    springs = "?".join([springs, springs, springs, springs, springs])
    record = ",".join([record, record, record, record, record])
    record = tuple(map(int, record.split(",")))

    springs = [i for i in springs.split(".") if len(i) > 0]

    return solve(springs, record)


print("p1", sum([solve_p1(i) for i in lines]))
print("p2", sum([solve_p2(i) for i in lines]))
