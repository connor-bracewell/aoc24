import sys

grid = []
with open(sys.argv[1]) as f:
  for line in f:
    grid.append(list(line.strip()))

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

best = [[[None, None, None, None, [], [], [], []] for c in line] for line in grid]
queue = []
queue.append([start_y, start_x, start_d, 0, None, None, None])
for y,x,d,s,py,px,pd in queue:
  if grid[y][x] == '#':
    # hit a wall
    continue
  current_best = best[y][x][d]
  if current_best is not None:
    if current_best < s:
      # found a better path already
      continue
    if current_best == s:
      best[y][x][d+4].append((py,px,pd))
      continue
  # found a new best
  best[y][x][d] = s
  best[y][x][d+4] = [(py,px, pd)]
  if grid[y][x] == 'E':
    # hit the end, don't keep traversing
    continue
  queue.append([y+dy[d], x+dx[d], d, s+1, y, x, d])
  # turn right
  dr = (d+1)%4
  queue.append([y, x, dr, s+1000, y, x, d])
  # turn left
  dl = (d-1)%4
  queue.append([y, x, dl, s+1000, y, x, d])
  # turn 180
  d180 = (d+2)%4
  queue.append([y, x, d180, s+2000, y, x, d])
queue2 = []
best_end = min(filter(lambda s: s is not None, best[end_y][end_x][:4]))
print(f'best score: {best_end}')
for i in range(4):
  if best[end_y][end_x][i] == best_end:
    queue2.append((end_y, end_x, i))
result = 0
for py,px,pd in queue2:
  if py is None:
    continue  # back at the starting square
  if grid[py][px] != 'O':
    grid[py][px] = 'O'
    result += 1
  queue2.extend(best[py][px][pd+4])
for line in grid:
  print(''.join(line))
print(f'{result}')
