import sys

with open(sys.argv[1]) as f:
  grid = [[int(c) for c in line.strip()] for line in f]
buckets = [[] for _ in range(10)]
for y,row in enumerate(grid):
  for x,n in enumerate(row):
    buckets[n].append((y,x))
reachable = [[0 for _ in row] for row in grid]
for y,x in buckets[9]:
  #print(f'9 at row {y} col {x}')
  reachable[y][x] = 1
for n in reversed(range(9)):
  for y,x in buckets[n]:
    if y > 0 and grid[y-1][x] == n+1:
      reachable[y][x] += reachable[y-1][x]
    if y+1 < len(grid) and grid[y+1][x] == n+1:
      reachable[y][x] += reachable[y+1][x]
    if x > 0 and grid[y][x-1] == n+1:
      reachable[y][x] += reachable[y][x-1]
    if x+1 < len(grid[y]) and grid[y][x+1] == n+1:
      reachable[y][x] += reachable[y][x+1]
result = 0
for y,x in buckets[0]:
  #print(f'0 at row {y} col {x} reaches {reachable[y][x]}')
  result += reachable[y][x]
print(f'{result}')
