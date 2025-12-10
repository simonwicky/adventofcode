#!/usr/bin/env python

import numpy as np
from scipy.optimize import milp, LinearConstraint

type Counters = list[int]
type Buttons = list[list[int]]


def parse_line(line: str) -> tuple[Counters, Buttons]:
    split_line = line.split()
    counters = [int(c) for c in split_line[-1][1:-1].split(",")]

    buttons: Buttons = []
    for button in split_line[1:-1]:
        buttons += [[int(b) for b in button[1:-1].split(",")]]

    return counters, buttons










def solve(counters : Counters, buttons: Buttons) -> int:

    # Formatting buttons into a matrix
    matrix_b = []
    for i in range(len(counters)):
        line = []
        for b in buttons:
            if i in b:
                line += [1]
            else:
                line += [0]
        matrix_b += [line]

    matrix_b = np.array(matrix_b)



    # Objective: minimize sum(x)
    c = np.ones(len(buttons))

    # All variables integer
    integrality = np.ones(len(buttons))

    # Enforce Bx = T
    constraint = LinearConstraint(matrix_b, counters, counters)

    res = milp(
        c=c,
        constraints=[constraint],
        integrality=integrality,
    )

    return sum(res.x)


    

with open('input','r') as f:
    data = f.read().splitlines()

total = 0

for line in data:
    counters, buttons = parse_line(line)
    total += int(solve(counters, buttons))
   

print(total)