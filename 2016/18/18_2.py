#!/usr/bin/env python

def next_row(line: str) -> str:
    # Adding safe tile left and right so bound checks become unneeded 
    extended_line = '.' + line + '.'

    new_line = ''
    for i in range(1, len(extended_line) - 1):
        previous_traps = extended_line[i-1:i+2]
        if previous_traps in ['^^.', '.^^', '^..','..^']:
            new_line += '^'
        else:
            new_line += '.'

    return new_line 

with open('input','r') as f:
    line = f.read()


total = line.count('.')
nb_rows = 400_000


for _ in range(nb_rows - 1):
    line = next_row(line)
    total += line.count('.')

print(total)