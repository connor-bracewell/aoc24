import sys

grid = []
moves = ''
with open(sys.argv[1]) as f:
  for l in f:
    if l == '\n':
      break
    grid.append(list(l.strip()))
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
  tx = rx+dx
  ty = ry+dy
  while grid[ty][tx] not in ['.','#']:
    tx += dx
    ty += dy
  if grid[ty][tx] == '#':
    # cast found a wall
    print('bonk!')
  else:
    # cast found an open square
    nx = rx + dx
    ny = ry + dy
    grid[ty][tx] = grid[ny][nx]
    grid[ry][rx] = '.'
    rx = nx
    ry = ny
    grid[ry][rx] = '@'
show()
result = 0
for y, row in enumerate(grid):
  for x, c in enumerate(row):
    if c == 'O':
      result += 100*y + x
print(f'{result}')
