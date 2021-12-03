#!/usr/bin/python3

import sys

datafile = sys.argv[1]

print("\n{:-^76}\n".format(" AoC 2021 - Day 3a "))
print("reading data from", datafile)

lines     = 0
char      = list()
gma       = list()
eps       = list()
gamma     = ""
gamma_d   = ""
epsilon   = ""
epsilon_d = ""
with open (datafile, 'r') as filename:
    data = filename.read().splitlines()
    for line in data:
        lines += 1
        if lines == 1:
            char =  [0]  * len(line)
            gma  = ["0"] * len(line)
            eps  = ["0"] * len(line)
        for n in range(len(line)):
            char[n] += int(line[n])
    for n in range(len(char)):
        if   char[n] > (lines / 2):
            gma[n] = str(1)
            eps[n] = str(0)
        elif char[n] < (lines / 2):
            gma[n] = str(0)
            eps[n] = str(1)
        else:
            gma[n] = "*"
    gamma     = ''.join(str(i) for i in gma)
    gamma_d   = int(gamma, 2)
    epsilon   = ''.join(str(i) for i in eps)
    epsilon_d = int(epsilon, 2)

print("--- lines:", lines, "\n    char   :", char,
      "\n    gamma  :", gma, gamma, gamma_d,
      "\n    epsilon:", eps, epsilon, epsilon_d,
      "\n\n    power consumption is: ", gamma_d * epsilon_d)
