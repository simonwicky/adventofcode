#!/usr/bin/env python

def expand(start_value: str, target_size: int) -> str:
    if len(start_value) >= target_size:
        return start_value[:target_size]

    b = ''.join(['1' if c == '0' else '0' for c in start_value[::-1]])

    return expand(start_value + '0' + b, target_size)
    
def checksum(value: str) -> str:
    if len(value) % 2 == 1:
        return value
    new_value = ''
    for i in range(len(value) // 2):
        if value[2 * i] == value[2* i + 1]:
            new_value += '1'
        else:
            new_value += '0'


    return checksum(new_value)


with open('input','r') as f:
    start_value = f.read()

target_size = 272

disk_data = expand(start_value, target_size)
print(checksum(disk_data))