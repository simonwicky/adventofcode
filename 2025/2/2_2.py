#!/usr/bin/env python

def invalid_id(n: int) -> bool:
    n_str = str(n)
    for i in range(1, (len(n_str) // 2) + 1):
        if len(n_str) % i == 0:
            if n_str == n_str[:i] * (len(n_str) // i): 
                return True
            
    return False


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