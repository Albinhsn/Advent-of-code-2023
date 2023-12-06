def parse_p1(line):
    return [int(i) for i in line.split(":")[1].strip().split()]


def parse_p2(line):
    return int("".join(line.split(":")[1].strip().split()))


def solve_p1():
    races = (lambda n: zip(parse_p1(n[0]), parse_p1(n[1])))(
        open("input").read().split("\n")[:-1]
    )
    p1 = 1
    for race in races:
        time, dist = race
        score = sum([1 for i in range(1, time) if i * (time - i) > dist])
        p1 *= score

    print(f"p1:{p1}")


def solve_p2():
    time, dist = (lambda n: (parse_p2(n[0]), parse_p2(n[1])))(
        open("input").read().split("\n")[:-1]
    )
    print(f"p2:{sum([1 for i in range(1, time) if i * (time - i) > dist])}")


solve_p1()
solve_p2()
