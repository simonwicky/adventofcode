#!/usr/bin/env python

import hashlib


with open('input','r') as f:
    salt = f.read()


def is_potential_key(digest : str):
    for i in range(len(digest)-2):
        if digest[i] == digest[i+1] and digest[i] == digest[i+2]:
            return digest[i]
    return None



potential_keys: list[tuple[int, str]] = []
keys: list[int] = []

nb_keys = 64

i = 0
while len(keys) < nb_keys:
    hash_input = salt + str(i)
    hash_result = hashlib.md5(hash_input.encode()).hexdigest()

    # Check if it confirms a key
    new_potential_keys: list[tuple[int, str]] = []
    for p_k in potential_keys:
        if 5*p_k[1] in hash_result:
            keys += [p_k[0]]
        elif i - p_k[0] < 1000:
            new_potential_keys += [p_k]
    potential_keys = new_potential_keys

    # Check if it's a potential key
    char = is_potential_key(hash_result)
    if char:
        potential_keys += [(i,char)]

    i += 1


print(sorted(keys)[nb_keys-1])


