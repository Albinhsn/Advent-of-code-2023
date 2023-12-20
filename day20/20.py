import math
import sys
from collections import defaultdict, deque

lines = open(sys.argv[1]).read().strip().split("\n")

modules = {}
for line in lines:
    module, targets = line.split(" -> ")
    targets = [i.strip() for i in targets.split(",")]
    if module[0] == "%":
        modules[module[1:]] = {"type": 0, "on": 0, "targets": targets}
    elif module[0] == "&":
        modules[module[1:]] = {
            "type": 1,
            "on": 0,
            "targets": targets,
            "last pulse": defaultdict(int),
        }
    else:
        modules[module] = {"type": 2, "targets": targets, "on": 0}

for key, val in modules.items():
    for target in val["targets"]:
        if target not in modules:
            continue
        if modules[target]["type"] == 1:
            modules[target]["last pulse"][key] = 0

presses = 0
L, H = 0, 0
p1, p2 = False, False
cycles = {}
while True:
    Q = deque([("broadcaster", 0, "btn")])
    presses += 1
    curr = []
    while Q:
        receiver, pulse, sender = Q.popleft()
        if receiver == "dd" and pulse == 1 and sender not in cycles:
            cycles[sender] = presses

        if len(cycles.keys()) == len(modules["dd"]["last pulse"].keys()) and not p2:
            print("p2", math.lcm(*list(cycles.values())))
            p2 = True

        if pulse == 0 and receiver == "rx":
            print("p2", presses)
            break

        if pulse == 1:
            H += 1
        else:
            L += 1

        if receiver not in modules:
            continue
        m = modules[receiver]
        if receiver != "broadcaster":
            if m["type"] == 0:
                if pulse == 0:
                    m["on"] = (m["on"] + 1) % 2
                    for target in m["targets"]:
                        Q.append((target, m["on"], receiver))
            else:
                m["last pulse"][sender] = pulse
                to_send = (
                    0
                    if len(m["last pulse"].keys()) == sum(m["last pulse"].values())
                    else 1
                )
                for target in m["targets"]:
                    Q.append((target, to_send, receiver))

        else:
            for target in m["targets"]:
                Q.append((target, 0, receiver))

    if presses == 1000 and not p1:
        print("p1", L * H)
        p1 = True
    if p1 and p2:
        break
