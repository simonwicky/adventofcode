#!/usr/bin/env python
"""
As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.
"""
import hashlib

with open('input','r') as f:
    room_id = f.read()

valid_index = "01234567"

i = 0
password = ["x"] * 8
print("".join(password),end='\r')
while "x" in password:
    hash_input = room_id + str(i)
    res = hashlib.md5(hash_input.encode()).hexdigest()
    if res[:5] == '00000':
        if res[5] in valid_index and password[int(res[5])] == 'x':
            password[int(res[5])] = res[6]
            print("".join(password),end='\r')
    i += 1


print("".join(password))