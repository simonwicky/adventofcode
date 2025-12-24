#!/usr/bin/env python


with open('input','r') as f:
    data = f.read().splitlines()

# Return the upper bound of the interval containing the ip, or none if it's not blocked
def is_blocked(blocked_ips: list[tuple[int, int]], ip: int):
    for ip_range in blocked_ips:
        if ip >= ip_range[0] and ip <= ip_range[1]:
            return ip_range[1]

    return None

blocked_ips: list[tuple[int, int]] = []

for line in data:
    lower_bound = line.split("-")[0]
    upper_bound = line.split("-")[1]
    blocked_ips += [(int(lower_bound), int(upper_bound))]


ip = 0
upper_bound = is_blocked(blocked_ips, ip)
while upper_bound:
    ip = upper_bound + 1
    upper_bound = is_blocked(blocked_ips, ip)

print(ip)