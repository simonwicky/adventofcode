#!/usr/bin/env python
"""
With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

def decrypt(name, sector_id):
    shift = sector_id % 26
    decrypted_name = ""
    for c in name:
        if c == " ":
            decrypted_name += " "
        else:
            dec_c = chr((ord(c) - 97 + shift) % 26 + 97)
            decrypted_name += dec_c
    

    return decrypted_name


with open('input','r') as f:
    data = f.read().splitlines()



for line in data:
    sep = line.index("[")
    split = line[:sep].split("-")
    name = " ".join(split[:-1])
    sector_id = int(split[-1])
    if "north" in decrypt(name, sector_id):
        print(sector_id)
        break
    
