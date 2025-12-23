#!/usr/bin/env python

# Chinese remainder theorem
def crt(a : list[int], n : list[int]):
    # We assume the modulis are co-prime
    big_n = 1
    for n_i in n:
        big_n *= n_i
    result = 0
    for i in range(len(a)):
        big_n_i = big_n // n[i]
        y_i = pow(big_n_i, -1, n[i])
        result += a[i] * y_i * big_n_i

    return result % big_n

# If I drop the capsule at time T, disc N should be at position 0 at time T+N
# At time T + N, a disc with P positions starting at X will be in position X + T + N mod P
# Hence I'm looking for T == -(N+X) mod P for all discs 


with open('input','r') as f:
    data = f.read().splitlines()


a: list[int] = []
n: list[int] = []
for line in data:
    split_line = line.split()
    modulo= int(split_line[3])
    offset = int(split_line[1][1:])
    start_position = int(split_line[-1][:-1])
    
    n += [modulo]
    a += [-(offset + start_position) % modulo]


print(crt(a,n))
