#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()



def compute(number_list, operand):
    if operand == '+':
        return sum(number_list)

    total = 1
    for n in number_list:
        total *= n
    return total 




grand_total = 0
numbers = []
operand = ''
for j in range(len(data[0])):
    maybe_number = ''.join([data[i][j] for i in range(4)])
    maybe_operand = data[4][j]
    if maybe_number == '    ':
        grand_total += compute(numbers, operand)
        numbers = []
        operand = ''
    else:
        numbers += [int(maybe_number)]
        if operand == '':
            operand = maybe_operand

grand_total += compute(numbers, operand)

print(grand_total)
