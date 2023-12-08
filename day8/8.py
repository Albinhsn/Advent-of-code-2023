import math


def lcm(a, b):
    print(a, b)
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


def parse_node(node):
    node = node.split("=")
    node[0] = node[0].strip()
    node[1] = node[1].replace("(", "").replace(")", "").strip().split(",")
    node[1][1] = node[1][1].strip()
    return node


def solve_p1():
    instructions, node = open("input").read().split("\n\n")
    nodes = [parse_node(i) for i in node.split("\n")[:-1]]
    node_map = {node[0]: {"left": node[1][0], "right": node[1][1]} for node in nodes}

    curr = "AAA"
    steps = 0
    while curr != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        if instruction == "L":
            curr = node_map[curr]["left"]
        else:
            curr = node_map[curr]["right"]
        steps += 1

    print(f"p1: {steps}")


def solve_p2():
    instructions, node = open("input").read().split("\n\n")
    nodes = [parse_node(i) for i in node.split("\n")[:-1]]
    node_map = {node[0]: {"left": node[1][0], "right": node[1][1]} for node in nodes}

    ends_in_a = [node[0] for node in nodes if node[0][-1] == "A"]
    node_with_z = {}
    for start in ends_in_a:
        curr = start
        steps = 0
        visited = {(curr, 0): 0}
        while True:
            instruction = instructions[steps % len(instructions)]
            if instruction == "L":
                curr = node_map[curr]["left"]
            else:
                curr = node_map[curr]["right"]
            steps += 1
            if (curr, steps % len(instructions)) not in visited:
                visited[(curr, steps % len(instructions))] = steps
            else:
                node_with_z[start] = [
                    (v, val) for v, val in visited.items() if v[0][-1] == "Z"
                ]
                break

    print(f"p2:{math.lcm(*[i[0][1] for i in node_with_z.values()])}")

solve_p1()
solve_p2()
