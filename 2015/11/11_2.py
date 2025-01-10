#!/usr/bin/env python
"""
Santa's password expired again. What's the next one?
"""


with open('input','r') as f:
    current_pwd = f.read()

allowed = 'abcdefghjkmnpqrstuvwxyz'

def incr(password):
    if len(password) == 0:
        return ""
    if password[-1] == allowed[-1]:
        return incr(password[:-1]) + allowed[0]
    return password[:-1] + allowed[allowed.index(password[-1]) + 1]

def first_req(password):
    for i in range(len(password) - 2):
        if ord(password[i + 2]) - ord(password[i + 1]) == 1 and ord(password[i + 1]) - ord(password[i]) == 1:
            return True
    return False

def last_req(password):
    first_double = ''
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if not first_double:
                first_double = password[i]
            else:
                if password[i] != first_double:
                    return True
    return False


new_pwd = incr(current_pwd)
while not (last_req(new_pwd) and first_req(new_pwd)):
    new_pwd = incr(new_pwd)

new_pwd = incr(new_pwd)
while not (last_req(new_pwd) and first_req(new_pwd)):
    new_pwd = incr(new_pwd)

print(new_pwd)