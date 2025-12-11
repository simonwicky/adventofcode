#!/usr/bin/env python

with open('input','r') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    numbers = [int(n) for n in line.split()]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if numbers[i] % numbers[j] == 0:
                total += numbers[i] // numbers[j]

print(total)