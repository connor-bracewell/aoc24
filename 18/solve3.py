import sys

char_open = '.'
char_wall = '#'
char_start = 's'
char_end = 'e'

with open(sys.argv[1]) as f:
  w,_ = map(int, f.readline().strip().split(' '))
  hits = []
  for l in f:
    x,y = map(int, l.strip().split(','))
    hits.append((x,y))

grid = [[char_open for _ in range(w+1)] for _ in range(w+1)]
for x,y in hits:
  grid[y][x] = char_wall

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
      nc = grid[ny][nx]
      if nc == char_start:
          fs = True
      elif nc == char_end:
          fe = True
      elif nc == char_open:
          maybequeue.append((nx,ny))
    if fs and fe:
      grid[y][x] = '@'
      return True
    elif fs:
      grid[y][x] = char_start
      queue.extend(maybequeue)
    elif fe:
      grid[y][x] = char_end
      queue.extend(maybequeue)
    else:
      grid[y][x] = char_open
  return False

if grid[0][0] != char_wall:
  fillfrom(0,0)
if grid[w][w] != char_wall:
  fillfrom(w,w)
show(grid)

def solve():
  # This assumes each tile is hit at most once...
  # If not, then do a pre-cleanup of later duplicates.
  for hx,hy in hits[::-1]:
    if fillfrom(hx,hy):
      return (hx,hy)

hx, hy = solve()
show(grid)
print(f'{hx},{hy}')
