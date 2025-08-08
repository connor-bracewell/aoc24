import sys

with open(sys.argv[1]) as f:
  w,bytecount = map(int, f.readline().strip().split(' '))
  hits = []
  for l in f:
    x,y = map(int, l.strip().split(','))
    hits.append((x,y))

grid = [['.' for _ in range(w+1)] for _ in range(w+1)]
prev = [[None for _ in range(w+1)] for _ in range(w+1)]

for x,y in hits[:bytecount]:
  grid[y][x] = '#'
grid[0][0] = '-'

def show():
  print('\n'.join([''.join(row) for row in grid]))
  print()

def solve():
  score = 0
  batch = [(0,0)]
  nbatch = []
  while batch:
    for y, x in batch:
      for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        if y == w and x == w:
          return
        ny = y+dy
        nx = x+dx
        if 0 <= ny <= w and 0 <= nx <= w and grid[ny][nx] == '.':
          prev[ny][nx] = (y,x)
          grid[ny][nx] = '-'
          nbatch.append((ny, nx))
    score += 1
    batch = nbatch
    nbatch = []

show()
solve()

tscore = 0
trace = (w,w)
while trace is not None:
  y,x = trace
  grid[y][x] = str(tscore%10)
  tscore += 1
  trace = prev[y][x]
show()
print(tscore-1)
