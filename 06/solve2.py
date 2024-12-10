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
  dx = [0,1,0,-1]
  dy = [-1,0,1,0]
  h = len(m)
  w = len(m[0])
  def check_loop(m,y,x,s):
    record = set()
    while True:
      if (x,y,s) in record:
        return True
      record.add((x,y,s))
      if y+dy[s]<0 or y+dy[s]>=h or x+dx[s]<0 or x+dx[s]>=w:
        return False
      if m[y+dy[s]][x+dx[s]] == '#':
        s = (s+1)%4
        continue
      x += dx[s]
      y += dy[s]
  result = 0
  s = 0  # initial state; up
  while True:
    m[y][x] = 'X'
    if y+dy[s]<0 or y+dy[s]>=h or x+dx[s]<0 or x+dx[s]>=w:
      break
    if m[y+dy[s]][x+dx[s]] == '.':
      m[y+dy[s]][x+dx[s]] = '#'
      if check_loop(m,y,x,(s+1)%4):
        result += 1
        if len(sys.argv) > 2:
          m[y+dy[s]][x+dx[s]] = 'O'
          print('found solution:')
          for line in m:
            print(''.join(line)) 
      m[y+dy[s]][x+dx[s]] = '.'
    if m[y+dy[s]][x+dx[s]] == '#':
      s = (s+1)%4
      continue
    x += dx[s]
    y += dy[s]
  if len(sys.argv) > 2:
    for line in m:
      print(''.join(line))
  print(f'{result}')
