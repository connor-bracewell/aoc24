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

cut = 100 if len(sys.argv) < 3 else int(sys.argv[2])

deltas = [(-1,0),(1,0),(0,-1),(0,1)]

def trace(x, y):
  out = [[-1 for _ in range(w)] for _ in range(h)]
  out[y][x] = 0
  score = 0
  queue = [(x,y)]
  while queue:
    nqueue =[]
    for x,y in queue:
      out[y][x] = score
      for dx,dy in deltas:
        nx = x+dx
        ny = y+dy
        if not (0 <= nx < w and 0 <= y < h):
          continue
        if out[ny][nx] == -1 and grid[ny][nx] != '#':
          out[ny][nx] = score
          nqueue.append((nx,ny))
    score += 1
    queue = nqueue
  return out

def ptrace(trace):
  for row in trace:
    print(''.join(map(lambda n: '-' if n < 0 else str(n%10), row)))
  print()

fwd = trace(start[0], start[1])
bwd = trace(end[0], end[1])
sp = fwd[end[1]][end[0]]

print(f'shortest path: {sp}; cut length {cut}')

ptrace(fwd)
ptrace(bwd)

result = 0
for x,y in product(range(w),range(h)):
  if fwd[y][x] >= 0:
    # Not a cheat spot.
    pass
  for bdx, bdy in deltas:
    for fdx, fdy in deltas:
      fx = x+fdx
      fy = y+fdy
      bx = x+bdx
      by = y+bdy
      if not (0 <= fx < w and 0 <= fy < h and 0 <= bx < w and 0 <= by < h):
        continue
      fd = fwd[fy][fx]
      bd = bwd[by][bx]
      if fd < 0 or bd < 0:
        continue
      cp = fd+bd+2
      saved = sp-cp
      if saved >= cut:
        print(f'cheat at ({fx},{fy})->({x},{y})->({bx},{by}) : {saved}')
        result += 1
print(f'{result}')
