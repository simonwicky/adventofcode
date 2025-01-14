#!/usr/bin/env python
"""
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""

mfcsam = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}


def format_line(line):
    sue_nb = int(line.split(" ")[1][:-1])
    attributes = {}
    line = line[line.index(": ") + 1:]
    line_split = line.split(",")
    for element in line_split:
        key = element.split(":")[0][1:]
        value = int(element.split(":")[1][1:])
        attributes[key] = value
    return sue_nb, attributes

def compatible(sue_attributes, mfcsam):
    greater_key = ["cats", "trees"]
    fewer_key = ["pomeranians", "goldfish"]
    for key in sue_attributes:
        if key in greater_key :
            if sue_attributes[key] <= mfcsam[key]:
                return False
        elif key in fewer_key:
            if sue_attributes[key] >= mfcsam[key]:
                return False
        elif sue_attributes[key] != mfcsam[key]:
            return False
    return True


with open('input','r') as f:
    data = f.read().splitlines()


for line in data:
    sue_nb, attributes = format_line(line)
    if compatible(attributes, mfcsam):
        print(sue_nb)
        break