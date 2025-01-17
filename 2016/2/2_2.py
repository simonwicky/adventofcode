#!/usr/bin/env python
"""
You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?
"""




with open('input','r') as f:
    data = f.read().splitlines()

def keypad(x,y):
    _keypad = [["X","X","1","X","X"],
            ["X","2","3","4","X",],
            ["5","6","7","8","9"],
            ["X","A","B","C","X"],
            ["X","X","D","X","X"]]
    if x < 0 or x >= len(_keypad) or y < 0 or y >= len(_keypad[x]):
        return 'X'
    return _keypad[x][y]

x,y = 2,0
code = ""
for line in data:
    for d in line:
        match d:
            case "L":
                new_y = y - 1
                y = new_y if keypad(x, new_y) != 'X' else y 
            case "R":
                new_y = y + 1
                y = new_y if keypad(x, new_y) != 'X' else y 
            case "U":
                new_x = x - 1
                x = new_x if keypad(new_x, y) != 'X' else x 
            case "D":
                new_x = x + 1
                x = new_x if keypad(new_x, y) != 'X' else x 
    code += keypad(x,y)
print(code)