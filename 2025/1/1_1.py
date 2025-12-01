#!/usr/bin/env python

with open('input','r') as f:
    data: list[str] = f.read().splitlines()

DIAL_SIZE = 100
dial_current = 50
password = 0

for line in data:
    nb_clicks = int(line[1:])
    direction = line[0]
    if direction == 'L':
        dial_current = (dial_current - nb_clicks) % DIAL_SIZE
    elif direction == 'R':
         dial_current = (dial_current + nb_clicks) % DIAL_SIZE

    if dial_current == 0:
        password += 1

print(password)
