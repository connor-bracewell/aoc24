import sys

with open(sys.argv[1]) as f:
  w,_ = map(int, f.readline().strip().split(' '))
  hits = []
  for l in f:
    x,y = map(int, l.strip().split(','))
    hits.append((x,y))

grid = [['.' for _ in range(w+1)] for _ in range(w+1)]
for x,y in hits:
  grid[y][x] = '#'

def show(grid):
  print('\n'.join([''.join(row) for row in grid]))
  print()

def fillfrom(hx,hy):
  queue = [(hx,hy)]
  fs = (hx,hy) == (0,0)
  fe = (hx,hy) == (w,w)
  for x,y in queue:
    maybequeue = []
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
      nx = x+dx
      ny = y+dy
      if not (0 <= nx <= w and 0 <= ny <= w):
        continue
      match grid[ny][nx]:
        case 'S':
          fs = True
        case 'F':
          fe = True
        case '.':
          maybequeue.append((nx,ny))
    if fs and fe:
      grid[y][x] = '@'
      return True
    elif fs:
      grid[y][x] = 'S'
      queue.extend(maybequeue)
    elif fe:
      grid[y][x] = 'F'
      queue.extend(maybequeue)
    else:
      grid[y][x] = '.'
  return False

if grid[0][0] != '#':
  fillfrom(0,0)
if grid[w][w] != '#':
  fillfrom(w,w)
show(grid)

def solve():
  # This assumes each tile is hit at most once...
  # If not, then do a pre-cleanup of later duplicates.
  for hx,hy in hits[::-1]:
    fs = False
    fe = False
    if hx == 0 and hy == 0:
      grid[0][0] = 'S'
      fs = True
    elif hx == w and hy == w:
      grid[w][w] = 'F'
      fe = True
    else:
      grid[hy][hx] = '.'
    if fillfrom(hx,hy):
      return (hx,hy)

hx, hy = solve()
show(grid)
print(f'{hx},{hy}')
