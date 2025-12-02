#!/usr/bin/env python

def invalid_id(n: int) -> bool:
    n_str = str(n)
    len_n = len(n_str)
    if len_n % 2 == 1:
        return False
    return n_str[:len_n // 2] == n_str[len_n // 2:]


def handle_range(r: str) -> int:
    a = int(r.split("-")[0])
    b = int(r.split("-")[1])

    total = 0
    for n in range(a,b+1):
        if invalid_id(n):
            total += n
    return total



with open('input','r') as f:
    data = f.read().split(",")

print(sum([handle_range(r) for r in data]))