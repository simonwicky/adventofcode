#!/usr/bin/env python
"""
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
"""
import re

#solve with AI cause my head hurts atm


with open('input','r') as f:
    data = f.read().splitlines()

def extract_sequences(ip):
    supernets = re.split(r'\[.*?\]', ip)  # Parts outside square brackets
    hypernets = re.findall(r'\[(.*?)\]', ip)  # Parts inside square brackets
    return supernets, hypernets

def find_aba(sequence):
    aba_patterns = []
    for i in range(len(sequence) - 2):
        if sequence[i] == sequence[i + 2] and sequence[i] != sequence[i + 1]:
            aba_patterns.append(sequence[i:i + 3])
    return aba_patterns

def supports_ssl(ip):
    supernets, hypernets = extract_sequences(ip)

    # Find all ABA patterns in supernets
    aba_patterns = []
    for supernet in supernets:
        aba_patterns.extend(find_aba(supernet))

    # Generate corresponding BAB patterns for each ABA
    bab_patterns = {aba[1] + aba[0] + aba[1] for aba in aba_patterns}

    # Check if any BAB pattern exists in the hypernets
    for hypernet in hypernets:
        for bab in bab_patterns:
            if bab in hypernet:
                return True

    return False


# Test the function
results = [1 for ip in data if supports_ssl(ip)]
print(sum(results))