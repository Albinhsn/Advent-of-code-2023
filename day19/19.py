import sys
from collections import deque


def solve_p2():
    def split_numbers_lt(x, m, a, s, var, Q):
        if var == "x":
            new_x = x[0], number - 1
            x = number, x[1]
            Q.append((new_x, m, a, s, dest))
        if var == "m":
            new_m = m[0], number - 1
            m = number, m[1]
            Q.append((x, new_m, a, s, dest))
        if var == "a":
            new_a = a[0], number - 1
            a = number, a[1]
            Q.append((x, m, new_a, s, dest))
        if var == "s":
            new_s = s[0], number - 1
            s = number, s[1]
            Q.append((x, m, a, new_s, dest))
        return x, m, a, s

    def split_numbers_gt(x, m, a, s, var, Q):
        if var == "x":
            new_x = number + 1, x[1]
            x = x[0], number
            Q.append((new_x, m, a, s, dest))
        elif var == "m":
            new_m = number + 1, m[1]
            m = m[0], number
            Q.append((x, new_m, a, s, dest))
        elif var == "a":
            new_a = number + 1, a[1]
            a = a[0], number
            Q.append((x, m, new_a, s, dest))
        else:
            new_s = number + 1, s[1]
            s = s[0], number
            Q.append((x, m, a, new_s, dest))
        return x, m, a, s

    Q = deque([((1, 4000), (1, 4000), (1, 4000), (1, 4000), "in")])

    workflows, _ = open(sys.argv[1]).read().strip().split("\n\n")
    workflows = [i.split("{") for i in workflows.split("\n")]
    workflows = {i[0]: i[1][:-1].split(",") for i in workflows}

    answer = 0
    while Q:
        x, m, a, s, curr = Q.popleft()
        M = {"x": x, "m": m, "a": a, "s": s}
        if curr == "A":
            answer += (
                (x[1] - x[0] + 1)
                * (m[1] - m[0] + 1)
                * (a[1] - a[0] + 1)
                * (s[1] - s[0] + 1)
            )
            continue
        if curr == "R":
            continue
        workflow = workflows[curr]
        for rule in workflow:
            if ":" in rule:
                rule, dest = rule.split(":")
                var, sign, number = rule[0], rule[1], int(rule[2:])
                if sign == "<":
                    if M[var][1] < number:
                        Q.append((x, m, a, s, dest))
                        break
                    if M[var][0] > number:
                        continue
                    x, m, a, s = split_numbers_lt(x=x, m=m, a=a, s=s, var=var, Q=Q)
                if sign == ">":
                    if M[var][0] > number:
                        Q.append((x, m, a, s, dest))
                        break
                    if M[var][1] < number:
                        continue
                    x, m, a, s = split_numbers_gt(x=x, m=m, a=a, s=s, var=var, Q=Q)

            else:
                Q.append((x, m, a, s, rule))
                break
    print(answer)


def solve_p1():
    workflows, parts = open(sys.argv[1]).read().strip().split("\n\n")
    workflows = [i.split("{") for i in workflows.split("\n")]
    workflows = {i[0]: i[1][:-1].split(",") for i in workflows}
    parts = parts.split("\n")

    answer = 0
    for part in parts:
        part = [i.split("=") for i in part[1:-1].split(",")]
        part = {i[0]: int(i[1]) for i in part}
        curr = "in"
        while True:
            print(curr, part)
            workflow = workflows[curr]
            for rule in workflow:
                if ":" in rule:
                    rule, dest = rule.split(":")
                    var, sign, number = rule[0], rule[1], int(rule[2:])
                    if sign == "<" and part[var] < number:
                        curr = dest
                        break
                    if sign == ">" and part[var] > number:
                        curr = dest
                        break

                else:
                    curr = rule
                    break
            if curr == "R":
                break
            elif curr == "A":
                answer += sum(part.values())
                break
    print("P1", answer)


solve_p1()
solve_p2()
