#!/usr/bin/env python

type Node = str
type Connections = dict[Node, list[Node]]

def parse_input():
    with open('input','r') as f:
        data = f.read().splitlines()

    connections: dict[Node, list[Node]] = {}

    for line in data:
        line = line.split()
        entry = line[0][:-1]
        connections[entry] = line[1:]

    return connections

def nb_paths(start: Node, target: Node, connections: Connections) -> int :
    def inner(current: dict[Node, int], target: Node, acc: int) -> int:
        if len(current) == 0:
            return acc
        new_current: dict[Node, int] = {}
        for n in current:
            for nxt in connections.get(n,[]):
                if nxt == target:
                    acc += current[n]
                else:
                    new_current[nxt] = new_current.get(nxt,0) + current[n]

        return inner(new_current, target, acc)
    
    return inner({start: 1}, target, 0)
    
connection = parse_input()
start = "you"
target = "out"

print(nb_paths(start, target, connection))

