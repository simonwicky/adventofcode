#!/usr/bin/env python
"""
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""


import json

with open('input','r') as f:
    document = json.load(f)

def sum_(obj):
    if type(obj) == str:
        return 0
    if type(obj) == int:
        return obj
    if type(obj) == list:
        return sum([sum_(i) for i in obj])
    if "red" in obj.values():
        return 0
    return sum([sum_(i) for i in obj.values()])



print(sum_(document))