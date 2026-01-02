#!/usr/bin/env python

class Program():
    def __init__(self, name: str, weight: int, children: list[str]):
        self.name = name
        self.weight = weight
        self.children = children


    @classmethod
    def from_line(cls, line: str):
        split_line = line.split()
        name = split_line[0]
        weight = int(split_line[1][1:-1])
        if len(split_line) > 2:
            children = split_line[3:]
        else: 
            children = []

        for i in range(len(children)):
            if children[i][-1] == ',':
                 children[i] = children[i][:-1]

        return cls(name, weight, children)   
    

    def sub_towers_weight(self) -> int:       
        return sum([programs[c].sub_towers_weight() for c in self.children]) + self.weight
    
    def is_balanced(self) -> bool:
        return len(set([programs[c].sub_towers_weight() for c in self.children])) == 1
    


with open('input','r') as f:
    data = f.read()

start_program = ''
for line in data.splitlines():
    if data.count(line.split()[0]) == 1:
        start_program = line.split()[0]


with open('input','r') as f:
    data = f.read().splitlines()

programs: dict[str, Program] = {}
for line in data:
    p = Program.from_line(line)
    programs[p.name] = p

poi = programs[start_program]

found = False
while not found:
    sub_towers = [programs[c].sub_towers_weight() for c in poi.children]
    for t in sub_towers:
        if sub_towers.count(t) == 1:
            idx = sub_towers.index(t)
            new_poi = programs[poi.children[idx]]

            if new_poi.is_balanced():
                offset = t - sub_towers[(idx + 1) % len(sub_towers)]
                print(new_poi.weight - offset)
                found = True
            poi = new_poi

            









# 1275