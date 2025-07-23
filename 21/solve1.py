import sys

codes = []
with open(sys.argv[1]) as f:
  for l in f:
    codes.append(l.strip())

def makelookup(kp):
  lookup = {}
  for y in range(len(kp)):
    for x in range(len(kp[y])):
      if kp[y][x] is not None:
       lookup[kp[y][x]] = (x,y)
  return lookup

def expp(cur, nxt, lookup):  
  xcur,ycur = lookup[cur]
  xnxt,ynxt = lookup[nxt]
  dx = xnxt-xcur
  dy = ynxt-ycur
  cr = 0 if dx < 0 else dx
  cu = 0 if dy > 0 else -dy
  cl = 0 if dx > 0 else -dx
  cd = 0 if dy < 0 else dy
  return cr,cu,cl,cd

lookup1 = makelookup([
  [ '7','8','9'],
  [ '4','5','6'],
  [ '1','2','3'],
  [None,'0','A'],
])
def exp1(code):
  inputs = ''
  for cur,nxt in zip('A'+code,code):
    cr,cu,cl,cd = expp(cur,nxt,lookup1)
    if lookup1[cur][1] == 3 and lookup1[nxt][0] == 0:
      # bottom row to leftmost column
      inputs += '^'*cu + '<'*cl + 'A'
    elif lookup1[cur][0] == 0 and lookup1[nxt][1] == 3:
      # leftmost column to bottom row
      inputs += '>'*cr + 'v'*cd + 'A' 
    else:
      inputs += '<'*cl + 'v'*cd + '>'*cr + '^'*cu + 'A'
  return inputs

lookup2 = makelookup([
  [None, '^', 'A'],
  [ '<', 'v', '>'],
])
def exp2(code):
  inputs = ''
  for cur,nxt in zip('A'+code,code):
    if cur == '^' and nxt == '<':
      inputs += 'v<A'
    elif cur == 'A' and nxt == '<':
      inputs += 'v<<A'
    else:
      cr,cu,cl,cd = expp(cur,nxt,lookup2)
      inputs += '<'*cl+'>'*cr+'v'*cd+'^'*cu+'A'
  return inputs

result = 0
for code in codes:
  print(code)
  inputs1 = exp1(code)
  print(inputs1)
  inputs2 = exp2(inputs1)
  print(inputs2)
  inputs3 = exp2(inputs2)
  print(inputs3)
  numpart = int(code[:-1])
  score = len(inputs3) * numpart
  print(f'{code} adds {len(inputs3)}*{numpart}={score}')
  result += score
print(f'{result}')
