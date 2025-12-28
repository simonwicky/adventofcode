#!/usr/bin/env python

with open('input','r') as f:
    print(sum([int(line) for line in f.read().splitlines()]))