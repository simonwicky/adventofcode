#!/usr/bin/env python
"""
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?
"""

def solvable(result, operands):
    if len(operands) == 1:
        return operands[0] == result
    
    # if last operand can't divide result, then it has to be a +
    if result % operands[-1] != 0:
        return solvable(result - operands[-1], operands[:-1])
    
    #test both cases
    return solvable(result - operands[-1], operands[:-1]) or solvable(result // operands[-1], operands[:-1])
    

equations = []
with open('input','r') as f:
    for line in f.read().splitlines():
        result = int(line.split(":")[0])
        numbers = [int(n) for n in line.split(":")[1].split(" ") if n]
        equations += [(result, numbers)]


total = 0
for equation in equations:
    if solvable(equation[0],equation[1]):
        total += equation[0]

print(total)