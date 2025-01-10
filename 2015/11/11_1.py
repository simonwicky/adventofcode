#!/usr/bin/env python
"""
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?
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

print(new_pwd)
