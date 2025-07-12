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
    d = 10_000_000_000_000
    cases.append(Case(int(xa), int(ya), int(xb), int(yb), int(xt)+d, int(yt)+d))
result = 0
for i, c in enumerate(cases):
  num = c.yb*c.xt - c.xb*c.yt
  den = c.yb*c.xa - c.xb*c.ya
  if den == 0:
    # None of the provided cases have a,b colinear.
    print(f'm[{i}] ERROR: colinear buttons!')
    continue
  if den < 0:
    num *= -1; den *= -1
  if abs(den) > abs(num) or num % den != 0:
    print(f'm[{i}] solution {num}/{den} has remainder {num % den}')
    continue
  ac = num//den
  xr = c.xt - ac*c.xa
  if xr % c.xb != 0:
    print(f'm[{i}] remainder {xr} not divisible by {xb}')
    continue
  bc = xr//c.xb
  print(f'm[{i}] Ax{ac} Bx{bc}')
  result += 3*ac + bc
print(f'{result}')
