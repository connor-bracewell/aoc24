import sys
import re

robots = []
with open(sys.argv[1]) as f:
  h = int(f.readline())
  w = int(f.readline())
  for l in f:
    x, y, dx, dy = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', l).groups()
    robots.append([int(y), int(x), int(dy), int(dx)])
print(h)
print(w)
for r in robots:
  print(f'{r[0]} {r[1]} {r[2]} {r[3]}')
steps = 100 % (h*w)
for r in robots:
  r[0] = (r[0] + steps * r[2]) % h
  r[1] = (r[1] + steps * r[3]) % w
quads = [0, 0, 0, 0]
for r in robots:
  if r[0] == h//2 or r[1] == w//2:
    continue
  quad = 0
  if r[0] > h//2:
    quad += 2
  if r[1] > w//2:
    quad += 1
  quads[quad] += 1
result = quads[0] * quads[1] * quads[2] * quads[3]
print(f'{result}')
