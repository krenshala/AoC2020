#!/usr/bin/python3

import sys

datafile = sys.argv[1]

print("\n{:-^76}\n".format(" AoC 2021 - Day 2a "))
print("reading data from", datafile)
depth = 0
position = 0
pos_change = 0
depth_change = 0
with open (datafile, 'r') as filename:
    while (data := filename.readline().rstrip()):
        command, change = data.split(" ")
        print(command, change, "units")
        if   command == "forward":
            position += int(change)
        elif command == "up":
            depth -= int(change)
        elif command == "down":
            depth += int(change)
        print("currently at {} units forward, {} units depth".format(position, depth))
print("final answer: ", position * depth)
