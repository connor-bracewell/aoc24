import sys
from itertools import product

start = None
end = None
grid = []
with open(sys.argv[1]) as f:
  for y, row in enumerate(f):
    gridrow = []
    for x, c in enumerate(row.strip()):
      match c:
        case 'S':
          start = (x,y)
        case 'E':
          end = (x,y)
      gridrow.append(c)
    grid.append(gridrow)
h = len(grid)
w = len(grid[0])

target = 100 if len(sys.argv) < 3 else int(sys.argv[2])
cheatlen = 20 if len(sys.argv) < 4 else int(sys.argv[3])

deltas = [(-1,0),(1,0),(0,-1),(0,1)]
def ok(x,y):
  return 0 <= x < w and 0 <= y < h

trace = [[-1 for _ in range(w)] for _ in range(h)]
score = 0
x,y = start
path = [(x,y)]
while True:
  trace[y][x] = score
  score += 1
  for dx,dy in deltas:
    nx = x+dx
    ny = y+dy
    if ok(nx,ny) and trace[ny][nx] == -1 and grid[ny][nx] != '#':
      x = nx
      y = ny
      path.append((x,y))
      break
  else:
    break
sp = trace[end[1]][end[0]]

print(f'shortest path: {sp}; target cut length {target}; allowed cheat length {cheatlen}')
for row in trace:
  print(''.join(map(lambda n: ' ' if n < 0 else f'\033[102m{n%10}\033[0m', row)))

def fd(x,y):
  return trace[y][x]
def bd(x,y):
  n = fd(x,y)
  return -1 if n<0 else sp-n

result = 0
for x,y in path:
  sd = fd(x,y)
  min_cx = max(-x, -cheatlen)
  max_cx = min(w-x, cheatlen+1)
  for dx in range(min_cx, max_cx):
    adx = abs(dx)
    remlen = cheatlen-abs(dx)
    min_cy = max(-y, -remlen)
    max_cy = min(h-y, remlen+1)
    for dy in range(min_cy, max_cy):
      ex = x+dx
      ey = y+dy
      ed = bd(ex,ey)
      if ed < 0:
        continue
      cp = sd + adx + abs(dy) + ed
      saved = sp - cp
      if saved >= target:
        # print(f'cheat ({x},{y})->({ex},{ey}) saves {saved}')
        result += 1
print(f'{result}')
