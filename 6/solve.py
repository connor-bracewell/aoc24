import sys

with open(sys.argv[1]) as f:
  m = [list(line.strip()) for line in f.readlines()]
  x = 0
  y = 0
  for sy,row in enumerate(m):
    for sx,val in enumerate(row):
      if val == '^':
        x=sx
        y=sy
        break
    else:
      continue
    break
  result = 0
  dx = 0
  dy = -1
  while True:
    if m[y][x] != 'X':
      result += 1
      m[y][x] = 'X'
    if y+dy<0 or y+dy>=len(m) or x+dx<0 or x+dx>=len(m[y+dy]):
      break
    if m[y+dy][x+dx] == '#':
      # turn right and try again
      ndx = -dy
      ndy = dx
      dy = ndy
      dx = ndx
      continue
    x += dx
    y += dy
  for line in m:
    print(''.join(line))
  print(f'{result}')
