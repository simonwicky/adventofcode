#!/usr/bin/env python
"""
The Historians sure are taking a long time. To be fair, the infinite corridors are very large.

How many stones would you have after blinking a total of 75 times?
"""

def blink(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        return [int(stone_str[:len(stone_str) // 2]),int(stone_str[len(stone_str) // 2:])]

    return [2024 * stone]




with open('input','r') as f:
    start_stones = [int(s) for s in f.read().splitlines()[0].split(" ")]

stone_count = {}
for stone in start_stones:
    stone_count[stone] = stone_count.get(stone,0) + 1


for i in range(75):
    new_stone_count = {}
    for stone, count in stone_count.items():
        new_stones = blink(stone)
        for new_stone in new_stones:
            new_stone_count[new_stone] = new_stone_count.get(new_stone,0) + count
    stone_count = new_stone_count


print(sum(stone_count.values()))
