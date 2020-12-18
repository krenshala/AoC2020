#!/usr/bin/python3

import re

ppdata = list()
with open("./day4.input", 'r') as day4data:
  line = day4data.readline()
  ppdata.append( dict() )
  while line:
    if not line == "\n":
      entries = line.split(' ')
      for entry in entries:
        key, value = entry.split(':')
        ppdata[-1].update({ key: value.strip()})
    else:
      ppdata.append( dict() )
    line = day4data.readline()

validpp = 0
for e in ppdata:
  valid = False
  hair  = re.compile("^#[0-9a-f]{6}$")
  hght  = re.compile("(\d+)(cm|in)")
  if len(e) > 7 or (len(e) == 7 and not "cid" in e.keys()):
    valid = True
  if valid and (int(e['byr']) < 1920 or int(e['byr']) > 2002):
    valid = False
  if valid and (int(e['iyr']) < 2010 or int(e['iyr']) > 2020):
    valid = False
  if valid and (int(e['eyr']) < 2020 or int(e['eyr']) > 2030):
    valid = False
  if valid and not hght.match(e['hgt']):
    valid = False
  elif valid and e['hgt']:
    h = hght.match(e['hgt'])
    if (h.group(2) == "cm" and (int(h.group(1)) < 150 or int(h.group(1)) > 193)) or (h.group(2) == "in" and (int(h.group(1)) < 59 or int(h.group(1)) > 76)):
      valid = False
  if valid and not hair.match(e['hcl']):
    valid = False
  if valid and e['ecl'] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
    valid = False
  if valid and (len(e['pid']) < 9 or len(e['pid']) > 9):
    valid = False
  if valid:
    validpp += 1
  
print("there are {} 'valid' passports!".format(validpp))
