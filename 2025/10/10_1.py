#!/usr/bin/env python

import itertools

type Lights = set[int]
type Buttons = list[list[int]]


def parse_line(line: str) -> tuple[Lights, Buttons]:
    split_line = line.split()
    lights: Lights = set()
    for i in range(len(split_line[0])):
        if split_line[0][i] == '#': 
            lights.add(i-1) #offset for the leading [

    buttons: Buttons = []
    for button in split_line[1:-1]:
        buttons += [[int(b) for b in button[1:-1].split(",")]]

    return lights, buttons


def correct(lights : Lights, buttons: Buttons) -> bool:
    final_lights: list[int] = []
    for b in buttons:
        for l in b:
            if l not in final_lights:
                final_lights += [l]
            else:
                final_lights.remove(l)
    return set(final_lights) == lights


with open('input','r') as f:
    data = f.read().splitlines()


total = 0
skip_rest = False

# Pressing a button more than once is useless as it results in a no-op

for line in data:
    lights, buttons = parse_line(line)
    for i in range(1,len(buttons) + 1):
        if skip_rest:
            skip_rest = False
            break
        for c in itertools.combinations(buttons,i):
            if correct(lights, list(c)):
                total += i
                skip_rest = True
                break

print(total)