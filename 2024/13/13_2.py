#!/usr/bin/env python
"""
As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error in your measurements, the position of every prize is actually 10000000000000 higher on both the X and Y axis!

Add 10000000000000 to the X and Y position of every prize. After making this change, the example above would now look like this:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take many more than 100 presses to do so.

Using the corrected prize coordinates, figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?
"""


def token(machine):

    x_a = int(machine[0][12:machine[0].index(",")])
    y_a = int(machine[0][machine[0].index("+",12)+1:len(machine[0])])

    x_b = int(machine[1][12:machine[1].index(",")])
    y_b = int(machine[1][machine[1].index("+",12)+1:len(machine[1])])

    x = 10000000000000 + int(machine[2][9:machine[2].index(",")])
    y = 10000000000000 + int(machine[2][machine[2].index("=",9)+1:len(machine[2])])

    button_b = ((x * y_a) - (x_a * y)) / ( (x_b * y_a ) - (x_a * y_b))
    button_a = (y - button_b * y_b) / y_a
    
    if int(button_a) == button_a and int(button_b) == button_b:
        return int(3 * button_a + button_b)

    return 0


machines = []

with open('input','r') as f:
    current_machine = []
    for line in f.read().splitlines():
        if line == "":
           machines += [current_machine]
           current_machine = []
        else:
            current_machine += [line]

    machines += [current_machine]

total = 0
for machine in machines:
    total += token(machine)
print(total)
