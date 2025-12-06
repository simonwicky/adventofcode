#!/usr/bin/env python

with open('input','r') as f:
    data = [line.split() for line in f.read().splitlines()]


grand_total = 0


for j in range(len(data[0])):
    if data[len(data)-1][j] == '+':
        grand_total += int(data[0][j]) + int(data[1][j]) + int(data[2][j]) + int(data[3][j])
    else:
        grand_total += (int(data[0][j]) * int(data[1][j]) * int(data[2][j]) * int(data[3][j]))
print(grand_total)