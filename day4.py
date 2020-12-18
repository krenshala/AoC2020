#!/usr/bin/python3


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

valid = 0
for entry in ppdata:
  if   len(entry) > 7 or (len(entry) == 7 and not "cid" in entry.keys()):
    valid += 1
print("there are {} 'valid' passports!".format(valid))
