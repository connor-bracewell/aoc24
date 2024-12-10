import sys

with open(sys.argv[1]) as f:
  grid = [[int(c) for c in line.strip()] for line in f]
buckets = [[] for _ in range(10)]
for y,row in enumerate(grid):
  for x,n in enumerate(row):
    buckets[n].append((y,x))
ymax = len(grid)-1
xmax = len(grid[0])-1
paths = [[1 if n == 9 else 0 for n in row] for row in grid]
for n in reversed(range(9)):
  for y,x in buckets[n]:
    if y > 0 and grid[y-1][x] == n+1:
      paths[y][x] += paths[y-1][x]
    if y < ymax and grid[y+1][x] == n+1:
      paths[y][x] += paths[y+1][x]
    if x > 0 and grid[y][x-1] == n+1:
      paths[y][x] += paths[y][x-1]
    if x < xmax and grid[y][x+1] == n+1:
      paths[y][x] += paths[y][x+1]
result = 0
for y,x in buckets[0]:
  #print(f'0 at row:{y} col:{x} has {paths[y][x]} paths')
  result += paths[y][x]
print(f'{result}')
