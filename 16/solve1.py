import sys

grid = []
with open(sys.argv[1]) as f:
  for line in f:
    grid.append(line.strip())

start_d = 0 # east, south, west, north
dy = [0,1,0,-1]
dx = [1,0,-1,0]
start_y = 0
start_x = 0
end_y = 0
end_x = 0
for y, row in enumerate(grid):
  for x, c in enumerate(row):
    if c == 'S':
      start_y = y
      start_x = x
    elif c == 'E':
      end_y = y
      end_x = x

best = [[[None, None, None, None] for c in line] for line in grid]
queue = []
queue.append([start_y, start_x, start_d, 0])
for y,x,d,s in queue:
  if grid[y][x] == '#':
    # hit a wall
    continue
  current_best = best[y][x][d]
  if current_best is not None and current_best <= s:
    # found a better path already
    continue
  best[y][x][d] = s
  if grid[y][x] == 'E':
    # hit the end, don't keep traversing
    continue
  queue.append([y+dy[d], x+dx[d], d, s+1])
  # turn right and step
  dr = (d+1)%4
  queue.append([y+dy[dr], x+dx[dr], dr, s+1001])
  # turn left and step
  dl = (d-1)%4
  queue.append([y+dy[dl], x+dx[dl], dl, s+1001])
  # turn 180 and step
  d180 = (d+2)%4
  queue.append([y+dy[d180], x+dx[d180], d180, s+2001])
result = min(filter(lambda s: s is not None, best[end_y][end_x]))
print(f'from r{start_y}c{start_x} to r{end_y}c{end_x}')
print(f'{result}')
