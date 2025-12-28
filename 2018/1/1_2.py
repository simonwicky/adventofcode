#!/usr/bin/env python
#!/usr/bin/env python

with open('input','r') as f:
    data = [int(line) for line in f.read().splitlines()]


current_freq = 0
frequencies: set[int] = set()
i = 0
while current_freq not in frequencies:
    frequencies.add(current_freq)
    current_freq += data[i % len(data)]
    i += 1

print(current_freq)