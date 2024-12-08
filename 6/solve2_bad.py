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
  record = [[ [False,False,False,False] for _ in line] for line in m]
  result = 0
  # initially facing up
  dx = 0
  dy = -1
  def udlr_idx(dy, dx):
    if dy == 1:
      return 0
    if dy == -1:
      return 1
    if dx == -1:
      return 2
    return 3
  while True:
    # remember we were here facing this direction
    record[y][x][udlr_idx(dy,dx)] = True
    m[y][x] = 'X'
    # if we were in the same spot facing (relatively) right before,
    # and haven't stepped through the next position already,
    # this is a solution
    if record[y][x][udlr_idx(dx,-dy)] and m[y+dy][x+dx] == '.':
      m[y+dy][x+dx] = 'O'
      print('found solution:')
      for line in m:
        print(''.join(line))
      result += 1
    # about to walk off the map; done
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
  print(f'{result}')
