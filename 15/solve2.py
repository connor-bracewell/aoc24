import sys

grid = []
moves = ''
with open(sys.argv[1]) as f:
  cmap = {
    '#':['#','#'],
    'O':['[',']'],
    '.':['.','.'],
    '@':['@','.'],
  }
  for l in f:
    if l == '\n':
      break
    row = []
    for c in l.strip():
      row.extend(cmap[c])
    grid.append(row)
  for l in f:
    moves += l.strip()

def show():
  for row in grid:
    print(''.join(row))
show()
print(f'{len(moves)} moves')

rx = 0
ry = 0
for y, row in enumerate(grid):
  for x, c in enumerate(row):
    if c == '@':
      rx=x;
      ry=y  
for m in moves:
  print(f'move: {m}')
  dx = 0
  dy = 0
  if m == '^':
    dy = -1
  elif m == '>':
    dx = 1
  elif m == 'v':
    dy = 1
  else: # <
    dx = -1
  if dx != 0:
    # horizontal move (simple)
    tx = rx+dx
    while grid[ry][tx] not in '#.':
      tx += dx
    if grid[ry][tx] == '#':
      print('bonk')
    else:
      while tx != rx:
        grid[ry][tx] = grid[ry][tx-dx]
        tx -= dx
      grid[ry][rx] = '.'
      rx = rx+dx
      grid[ry][rx] = '@'
  else:
    # vertical move (complicated!)
    def cast(x,y,dy):
      # if true, tile (x,y) can move dy
      c = grid[y][x]
      if c in '.{}':
        return True
      if c == '[':
        grid[y][x] = '{'
        grid[y][x+1] = '}'
        if cast(x,y+dy,dy) and cast(x+1,y+dy,dy):
          return True
      elif c == ']':
        grid[y][x] = '}'
        grid[y][x-1] = '{'
        if cast(x,y+dy,dy) and cast(x-1,y+dy,dy):
          return True
      elif c == '@':
        return cast(x,y+dy,dy)
      return False  # us or child hit a wall
    def revert(x,y,dy):
      # cast failed; clean up markers
      c = grid[y][x]
      if c == '{':
        grid[y][x] = '['
        grid[y][x+1] = ']'
        revert(x,  y+dy,dy)
        revert(x+1,y+dy,dy)
      elif c == '}':
        grid[y][x] = ']'
        grid[y][x-1] = '['
        revert(x,  y+dy,dy)
        revert(x-1,y+dy,dy)
    def commit(x,y,dy):
      # move children, then yourself
      c = grid[y][x]
      if c == '.':
        return
      if c == '{':
        commit(x,y+dy,dy)
        commit(x+1,y+dy,dy)
        grid[y+dy][x] = '['
        grid[y+dy][x+1] = ']'
        grid[y][x] = '.'
        grid[y][x+1] = '.'
        return
      if c == '}':
        commit(x,y+dy,dy)
        commit(x-1,y+dy,dy)
        grid[y+dy][x] = ']'
        grid[y+dy][x-1] = '['
        grid[y][x] = '.'
        grid[y][x-1] = '.'
        return
    if cast(rx,ry,dy):
      commit(rx,ry+dy,dy)
      grid[ry][rx] = '.'
      ry = ry+dy
      grid[ry][rx] = '@'
    else:
      revert(rx,ry+dy,dy)
      print('bonk')
  show()
result = 0
for y, row in enumerate(grid):
  for x, c in enumerate(row):
    if c == '[':
      result += 100*y + x
print(f'{result}')
