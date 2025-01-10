#!/usr/bin/env python
"""
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
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

w,g, target_wire = parse_input(data,'a')
w,g = solve_circuit(w,g)

print(w[target_wire])