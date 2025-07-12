import sys
import re
from dataclasses import dataclass

@dataclass
class Robot:
  x: int
  y: int
  dx: int
  dy: int

robots = []
with open(sys.argv[1]) as f:
  h = int(f.readline())
  w = int(f.readline())
  for l in f:
    x, y, dx, dy = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', l).groups()
    robots.append(Robot(int(x), int(y), int(dx), int(dy)))
for i in range(w*h):
  grid = [[0 for _ in range(w)] for _ in range(h)]
  for r in robots:
    grid[r.y][r.x] += 1
    r.x = (r.x + r.dx) % w
    r.y = (r.y + r.dy) % h
  if all([all([c<2 for c in row]) for row in grid]):
    for y in range(h//2):
      for x in range(w):
        has_robot = (grid[2*y][x] != 0 or grid[2*y+1][x] != 0)
        print('X' if has_robot else '.', end='')
      print('')
    print(f'@{i} - press enter to continue...')
    sys.stdin.readline()
