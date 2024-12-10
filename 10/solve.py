import sys

with open(sys.argv[1]) as f:
  grid = [[int(c) for c in line.strip()] for line in f]
  reachable = [[set() for _ in row] for row in grid]
  result = 0
  for i in range(10)[::-1]:
    for y,row in enumerate(grid):
      for x,n in enumerate(row):
        if n != i:
          continue
        if n == 9:
          print(f'9 at row {y} col {x}')
          reachable[y][x].add((y,x))
          continue
        for diff in [(1,0),(-1,0),(0,1),(0,-1)]:
          yp = y+diff[0]
          xp = x+diff[1]
          if 0<=yp<len(grid) and 0<=xp<len(row) and grid[yp][xp] == n+1:
            reachable[y][x] |= reachable[yp][xp]
        if n == 0:
          print(f'0 at row {y} col {x} reaches {reachable[y][x]}')
          result += len(reachable[y][x])
  print(f'{result}')
