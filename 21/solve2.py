import sys
from functools import cache

codes = []
with open(sys.argv[1]) as f:
  for l in f:
    codes.append(l.strip())

# For a given keypad, build an index c -> (x,y).
def makelookup(kp):
  lookup = {}
  for y, row in enumerate(kp):
    for x, c in enumerate(row):
      if c is not None:
        lookup[c] = (x,y)
  return lookup

# For two characters, get the left/right and up/down
# distance between them in the given lookup. 
def dxy(cur, nxt, lookup):  
  xcur,ycur = lookup[cur]
  xnxt,ynxt = lookup[nxt]
  dx = xnxt-xcur
  dy = ynxt-ycur
  dr =  dx if dx > 0 else 0
  du = -dy if dy < 0 else 0
  dl = -dx if dx < 0 else 0
  dd =  dy if dy > 0 else 0
  return dr,du,dl,dd

lookup1 = makelookup([
  [ '7','8','9'],
  [ '4','5','6'],
  [ '1','2','3'],
  [None,'0','A'],
])

def exp1(code):
  inputs = []
  # Expand the numeric code into the upstream directional inputs.
  # Assume the pointer starts on 'A'.
  for cur,nxt in zip('A'+code,code):
    dr,du,dl,dd = dxy(cur,nxt,lookup1)
    if lookup1[cur][1] == 3 and lookup1[nxt][0] == 0:
      # Moving bottom row to leftmost column;
      # go up-left to avoid the empty corner.
      inputs.append('^'*du + '<'*dl + 'A')
    elif lookup1[cur][0] == 0 and lookup1[nxt][1] == 3:
      # Moving leftmost column to bottom row;
      # go right-down to avoid the empty corner.
      inputs.append('>'*dr + 'v'*dd + 'A')
    else:
      inputs.append('<'*dl  + 'v'*dd + '^'*du + '>'*dr + 'A')
  return inputs

lookup2 = makelookup([
  [None, '^', 'A'],
  [ '<', 'v', '>'],
])

@cache
def exp2(code):
  inputs = []
  # Expand the directional code into the upstream directional inputs.
  # Assume the pointer starts on 'A'.
  for cur,nxt in zip('A'+code,code):
    # 4 special cases to avoid the empty corner.
    if cur == '^' and nxt == '<':
      inputs.append('v<A')
    elif cur == 'A' and nxt == '<':
      inputs.append('v<<A')
    elif cur == '<' and nxt == 'A':
      inputs.append('>>^A')
    elif cur == '<' and nxt == '^':
      inputs.append('>^A')
    else:
      cr,cu,cl,cd = dxy(cur,nxt,lookup2)
      inputs.append('<'*cl +  'v'*cd + '^'*cu + '>'*cr + 'A')
  print(f'{code} expands to {','.join(inputs)}')
  return inputs

@cache
def explen(dseq, n):
  # For the top-level keypad, the length of the necessary inputs is just the
  # length of the inputs themselves. Otherwise it's the sum of the lengths
  # of the inputs to the next-higher keypad.
  return len(dseq) if n == 0 else sum([explen(nseq, n-1) for nseq in exp2(dseq)])

result = 0
for code in codes:
  dinputs = exp1(code)
  print(f'{code} expands to {','.join(dinputs)}')
  flen = sum([explen(dinput, 25) for dinput in dinputs])
  numpart = int(code[:-1])
  score = flen * numpart
  print(f'{code} adds {flen}*{numpart}={score}\n')
  result += score
print(f'{result}')
