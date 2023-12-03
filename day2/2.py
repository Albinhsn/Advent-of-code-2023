from functools import reduce

RED = 12
GREEN = 13
BLUE = 14

COLOR_MAP = {"blue": BLUE, "red": RED, "green": GREEN}


def solve_p1(line) -> int:
    for s in line[1].split(";"):
        balls = s.split(",")
        for ball in balls:
            amount, color = ball.split()
            if int(amount) > COLOR_MAP[color]:
                return 0
    return int(line[0].split(" ")[1])


def solve_p2(line) -> int:
    min_map = {"red": 0, "blue": 0, "green": 0}
    for s in line[1].split(";"):
        balls = s.split(",")
        for ball in balls:
            amount, color = ball.split()
            min_map[color] = max(int(amount), min_map[color])
    return reduce(lambda x, y: x * y, min_map.values())


contents = open("./input").read().split("\n")[:-1]
game = [x.split(":") for x in contents]
print("p1", sum([solve_p1(line) for line in game]))
print("p2", sum([solve_p2(line) for line in game]))
