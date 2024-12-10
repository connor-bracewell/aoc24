import sys
import re

with open(sys.argv[1]) as f:
  result = 0;
  for (a,b) in re.findall(r"mul\((\d+),(\d+)\)", f.read()):
    result += int(a)*int(b)
  print(result)
