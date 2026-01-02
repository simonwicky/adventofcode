#!/usr/bin/env python

with open('input','r') as f:
    data = [int(memory) for memory in f.read().split()]



def reallocate(memory_bank: list[int]):
    i = memory_bank.index(max(memory_bank))
    to_reallocate = memory_bank[i]
    memory_bank[i] = 0
    for n in range(to_reallocate):
        memory_bank[(i + n + 1) % len(memory_bank)] += 1

    return memory_bank


seen: set[str] = set()

step = 0
while ','.join([str(d) for d in data]) not in seen:
    seen.add(','.join([str(d) for d in data]))
    data = reallocate(data)
    step += 1

print(step)