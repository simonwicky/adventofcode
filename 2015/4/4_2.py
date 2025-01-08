#!/usr/bin/env python

"""
Now find one that starts with six zeroes.
"""

import hashlib



with open('input','r') as f:
    secret_key = f.read()


i = 0
res = '111111'
while res[:6] != '000000':
    i += 1
    hash_input = secret_key + str(i)
    res = hashlib.md5(hash_input.encode()).hexdigest()


print(i)