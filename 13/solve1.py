import sys
import re
from dataclasses import dataclass

@dataclass
class Case:
  xa:int; ya:int
  xb:int; yb:int
  xt:int; yt:int

cases = []
with open(sys.argv[1]) as f:
  while l1 := f.readline():
    xa, ya = re.match(r'Button A: X\+(\d+), Y\+(\d+)', l1).groups()
    xb, yb = re.match(r'Button B: X\+(\d+), Y\+(\d+)', f.readline()).groups()
    xt, yt = re.match(r'Prize: X=(\d+), Y=(\d+)', f.readline()).groups()
    f.readline()
    cases.append(Case(int(xa), int(ya), int(xb), int(yb), int(xt), int(yt)))
result = 0
for i, c in enumerate(cases):
  machid = i+1
  num = c.yb*c.xt - c.xb*c.yt
  den = c.yb*c.xa - c.xb*c.ya
  if den == 0:
    # IIRC I checked before and none of the cases have a,b colinear.
    print(f'mach {machid}: colinear_error')
    continue
  if abs(den) > abs(num) or num % den != 0:
    print(f'mach {machid}: solution {num}/{den} non integer')
    continue
  ac = num//den
  xr = c.xt - ac*c.xa
  if xr % c.xb != 0:
    print(f'mach {machid}: remainder {xr} not divisible by {xb}')
    continue
  bc = xr//c.xb
  print(f'mach {i+1}: {ac}xA {bc}xB')
  result += 3*ac + bc
print(f'{result}')
