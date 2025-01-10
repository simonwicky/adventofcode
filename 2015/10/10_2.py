#!/usr/bin/env python
"""
Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).
https://www.youtube.com/watch?v=ea7lJkEhytA

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
"""
import itertools


def look_and_say(number):
    res = ''
    for k, g in itertools.groupby(number):
        res += str(len(list(g))) + k
    return res



with open('input','r') as f:
    start_number = f.read()

for _ in range(50):
    start_number = look_and_say(start_number)

print(len(start_number))
