#!/usr/bin/env python
"""
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""

with open('input','r') as f:
    data = f.read().splitlines()


def abba(string):
    for i in range(len(string)-3):
        if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
            return True
    return False

def bracket_abba(string):
    looking = False
    for i in range(len(string)-3):
        if looking and string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
            return True 
        if string[i] == "[":
            looking = True
        if string[i] == "]":
            looking = False
    return False

total = 0
for address in data:
   if abba(address) and not bracket_abba(address):
       total += 1
print(total)
