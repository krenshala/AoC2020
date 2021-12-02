#!/usr/bin/python3

import sys

datafile = sys.argv[1]

print("\n{:-^76}\n".format(" AoC 2021 - Day 1a "))
print("reading data from", datafile)
depth = 0
depth_change = 0
with open (datafile, 'r') as filename:
    while (data := filename.readline().rstrip()):
        data = int(data)
        if depth > 0 and data > depth:
            depth_change += 1
        depth = data
print("depth changes:",depth_change)
