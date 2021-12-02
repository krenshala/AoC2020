#!/usr/bin/python3

import sys

datafile = sys.argv[1]

print("\n{:-^76}\n".format(" AoC 2021 - Day 2b "))
print("reading data from", datafile)
aim = 0
depth = 0
position = 0
pos_change = 0
depth_change = 0
with open (datafile, 'r') as filename:
    while (data := filename.readline().rstrip()):
        command, change = data.split(" ")
        change = int(change)
        print("=> {} {} units".format(command, change))
        if   command == "up":
            aim -= change
        elif command == "down":
            aim += change
        elif command == "forward":
            position += change
            depth += (aim * change)
        print("currently at {} units forward, {} units depth ({} aim)".format(position, depth, aim))
print("final answer: ", position * depth)
