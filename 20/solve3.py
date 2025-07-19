import sys

start = None
grid = []
with open(sys.argv[1]) as f:
  for y, row in enumerate(f):
    gridrow = list(row.strip())
    grid.append(gridrow)
    for x, c in enumerate(gridrow):
      if c == 'S':
        start = (x,y)
h = len(grid)
w = len(grid[0])

target = 100 if len(sys.argv) < 3 else int(sys.argv[2])
cheatlen = 20 if len(sys.argv) < 4 else int(sys.argv[3])

deltas = [(-1,0),(1,0),(0,-1),(0,1)]
def ok(x,y):
  return 0 <= x < w and 0 <= y < h

trace = [start]
while True:
  x,y = trace[-1]
  for dx,dy in deltas:
    nx = x+dx
    ny = y+dy
    if ok(nx,ny) and grid[ny][nx] in '.E':
      trace.append((nx,ny))
      grid[ny][nx] = 'X'
      break
  else:
    break

result = 0
for i, (x,y) in enumerate(trace):
  for j, (ex,ey) in enumerate(trace[i+target:]):
    d = abs(x-ex) + abs(y-ey)
    if d > cheatlen:
      continue
    saved = j-d
    if saved >= 0:
      # print(f'cheat ({x},{y})->({ex},{ey}) saves {saved+target}')
      result += 1
print(f'{result}')
