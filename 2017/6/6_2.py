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

def key(memory_bank: list[int]):
    return ','.join([str(d) for d in data])


seen_with_step: dict[str, int] = {}

step = 0
while key(data) not in seen_with_step:
    seen_with_step[key(data)] = step
    data = reallocate(data)
    step += 1



print(step - seen_with_step[key(data)])