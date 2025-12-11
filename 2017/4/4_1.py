#!/usr/bin/env python


with open('input','r') as f:
    data = f.read().splitlines()

valid = 0
for passphrase in data:
    words = passphrase.split()
    if len(set(words)) == len(words):
        valid += 1

print(valid)