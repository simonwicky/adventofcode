#!/usr/bin/env python

"""
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

"""

def report_safe(report):
    index = is_safe(report)
    if index == -1:
        return True
    
    #brute_force all removals possible
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report) == -1:
            return True
    
    return False



def is_safe(report):
    diff = [i - j for i,j in zip(report[:-1],report[1:])]
    if diff[0] > 0:
        for i in range(len(diff)):
            if diff[i] < 1 or diff[i] > 3:
                return i
        return -1
    elif diff[0] < 0:
        for i in range(len(diff)):
            if diff[i] > -1 or diff[i] < -3:
                return i
        return -1
    return 0



total = 0
with open('input','r') as f:
    for line in f:
        report = [int(i) for i in line.split(" ")]
        if report_safe(report) :
            total += 1

print(total)
