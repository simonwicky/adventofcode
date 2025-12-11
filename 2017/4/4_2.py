#!/usr/bin/env python


with open('input','r') as f:
    data = f.read().splitlines()



def valid(passphrase: str) -> bool:
    word_list = passphrase.split()
    existing = []
    for word in word_list:
        sorted_word = sorted(list(word))
        if sorted_word in existing:
            return False
        else:
            existing += [sorted_word]

    return True




print(sum([1 for passphrase in data if valid(passphrase)]))