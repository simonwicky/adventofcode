#!/usr/bin/env python
"""
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""


def and_(op1, op2):
    return op1 & op2

def or_(op1, op2):
    return op1 | op2

def lshift(op1, op2):
    return op1 << op2

def rshift(op1, op2):
    return op1 >> op2

def not_(op1, _):
    return ~ op1


def get(wires, key):
    if type(key) == str:
        return wires[key]
    return key

def parse_input(data, target):
    wires = {}
    gates = []
    target_wire = ''
    for i in range(len(data)):
        gate = data[i].split(" ")
        if len(gate) == 3:
            if gate[2] == target:
                target_wire = gate[0]
            else:
                wires[gate[2]] = int(gate[0])
        elif gate[0] == 'NOT':
            gates += [(gate[1], None, not_, gate[3])]
        else:
            op1 = gate[0] if not gate[0].isdigit() else int(gate[0])
            op2 = gate[2] if not gate[2].isdigit() else int(gate[2])
            res = gate[4]
            match gate[1]:
                case 'AND':
                    op = and_
                case 'OR':
                    op = or_
                case 'RSHIFT':
                    op = rshift
                case 'LSHIFT':
                    op = lshift
            gates += [(op1, op2, op, res)]
    return wires, gates, target_wire

def solve_circuit(wires, gates):
    for i in range(len(gates)):
        gate = gates[i]
        if ((gate[0] in wires or type(gate[0]) == int) and
            (gate[1] in wires or type(gate[1]) == int or gate[1] == None)
        ):
            op1 = get(wires,gate[0])
            op2 = get(wires,gate[1])
            res_value = gate[2](op1, op2) & 65535
            wires[gate[3]] = res_value
            gates.pop(i)
            return solve_circuit(wires, gates)
        
    return wires, gates


with open('input','r') as f:
    data = f.read().splitlines()

#part 1
w,g, target_wire = parse_input(data,'a')
w,g = solve_circuit(w,g)

#part2
w2,g2, target_wire = parse_input(data,'a')
w2['b'] = w[target_wire]
w2,g2 = solve_circuit(w2,g2)

print(w2[target_wire])