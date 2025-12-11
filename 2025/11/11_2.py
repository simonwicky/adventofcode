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

# Nb of paths from svr to out via fft and dac = nb paths from svr to fft * nb paths from fft to dac * nb of paths from dac to out

# There are no ["dac", "fft"] paths, otherwise, we would have cycles and an infinite number of paths

possible_path = ["svr", "fft", "dac", "out"]

total = 1
for i in range(len(possible_path) - 1):
    nb_paths_segment = nb_paths(possible_path[i], possible_path[i+1], connection)
    # print("From " + path[i] + " to " + path[i+1] + ": " + str(nb_paths_segment))
    total *= nb_paths_segment


print(total)