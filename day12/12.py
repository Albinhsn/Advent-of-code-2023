lines = open("ex").read().split("\n")[:-1]


def solve_p1(line):
    def solve(springs, record) -> int:
        if not springs or not record:
            if [i for i in springs if "#" in i]:
                return 0
            out = 0 if record else 1
            if out:
                print("\t+1")
            return out
        score = 0
        curr, rest = record[0], record[1:]
        for i in range(len(springs)):
            if curr > len(springs[i]):
                if "#" in springs[i]:
                    return score
                score += solve(springs[i + 1 :], record)
                return score
            elif curr == len(springs[i]):
                print("2: ", curr, springs[i + 1 :], rest, springs[i])
                score += solve(springs[i + 1 :], rest)
            else:
                spring = springs[i]
                for j in range(len(spring) - curr):
                    if spring[curr + j] != "#":
                        if curr + j + 1 >= len(spring):
                            print("3: ", curr, springs[i + 1 :], rest, spring)
                            score += solve(springs[i + 1 :], rest)
                        elif spring[curr + j + 1] == "#":
                            return score
                        else:
                            springs[i] = spring[j + curr + 1 :]
                            print("4: ", curr, springs[i:], rest, spring)
                            score += solve(springs[i:], rest)
                    elif spring[j] == "#":
                        return score
                if "#" in spring:
                    return score

        return score

    springs, record = line.split()
    record = list(map(int, record.split(",")))
    springs = [i for i in springs.split(".") if len(i) > 0]

    return solve(springs, record)


print("p1", [solve_p1(i) for i in lines])
