import sys
import re

with open(sys.argv[1]) as f:
  result = 0;
  do = True
  for (a,b,isdo,isdont) in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", f.read()):
    if a and b and do:
      result += int(a)*int(b)
    if isdo:
      do = True
    if isdont:
      do = False
  print(result)
