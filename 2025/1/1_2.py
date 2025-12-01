#!/usr/bin/env python

with open('input','r') as f:
    data: list[str] = f.read().splitlines()

DIAL_SIZE = 100
dial_current = 50
password = 0

for line in data:
    nb_clicks = int(line[1:])
    direction = line[0]
    if direction == 'L':
        dial_new = dial_current - nb_clicks
        # We don't touch 0 at all
        if dial_new > 0:
            dial_current = dial_new
        else:
            # we actually crossed 0 without starting on it
            if dial_current != 0:
                password += 1 # we crossed 0
            
            password += abs(dial_new) // DIAL_SIZE
        
        dial_current = dial_new % DIAL_SIZE

        
    # No corner case there
    elif direction == 'R':
        dial_new = dial_current + nb_clicks
        password += dial_new // DIAL_SIZE

        dial_current = dial_new % DIAL_SIZE

print(password)