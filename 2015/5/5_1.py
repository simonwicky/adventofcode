#!/usr/bin/env python

"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

"""

import re

with open('input','r') as f:
    word_list = f.read().splitlines()

three_vowels = r'\w*[aeiou]\w*[aeiou]\w*[aeiou]\w*'
repeated = r'(\w)\1'
forbidden = r'ab|cd|pq|xy'


total = 0
for word in word_list:
    if re.search(three_vowels, word) and re.search(repeated, word) and not re.search(forbidden, word):
        total += 1

print(total)