#!/usr/bin/env python
"""
The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?
"""


with open('input','r') as f:
    target = int(f.read())

target = target // 11
houses = [0] * target;
houseNumber = target;

for i in range(1,target):

  visits = 0
  for j in range(1,51):
    if j * i < target:
        houses[j * i] += i
        if houses[j * i] >= target and (j * i) < houseNumber:
            houseNumber = j * i


print(houseNumber)
