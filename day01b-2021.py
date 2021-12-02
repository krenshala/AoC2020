#!/usr/bin/python3

import sys

datafile = sys.argv[1]

print("\n{:-^76}\n".format(" AoC 2021 - Day 1b "))
print("reading data from", datafile)
depth = 0
rolling_depth = list()
old_depth = 0
new_depth = 0
depth_change_a = 0
depth_change_b = 0
with open (datafile, 'r') as filename:
    while (data := filename.readline().rstrip()):
        data = int(data)
        # day 1a solution code
        if depth > 0 and data > depth:
            depth_change_a += 1
        depth = data
        # day 1b solution code
        rolling_depth.append(data)
        if len(rolling_depth) >= 3:
            new_depth = rolling_depth[-1] + rolling_depth[-2] + rolling_depth[-3]
            if old_depth > 0 and (new_depth - old_depth) > 0:
                depth_change_b += 1
        old_depth = new_depth
        print(rolling_depth[-3:], new_depth - old_depth)
print("\nsdepth changes:", depth_change_a, " rolling window changes:", depth_change_b)

