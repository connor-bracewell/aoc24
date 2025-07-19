import sys

with open(sys.argv[1]) as f:
  w,_ = map(int, f.readline().strip().split(' '))
  hits = []
  for l in f:
    x,y = map(int, l.strip().split(','))
    hits.append((x,y))

# Return True IFF there is a path through `grid`.
def solve(grid):
  batch = [(0,0)]
  nbatch = []
  while batch:
    for y, x in batch:
      if y == w and x == w:
        return True
      for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        ny = y+dy
        nx = x+dx
        if 0 <= ny <= w and 0 <= nx <= w and grid[ny][nx] == '.':
          grid[ny][nx] = 'O'
          nbatch.append((ny, nx))
    batch = nbatch
    nbatch = []
  return False

# Return True IFF there is a path through the grid after `bytecount` bytes of corruption.
def tryat(bytecount):
  grid = [['.' for _ in range(w+1)] for _ in range(w+1)]
  for x,y in hits[:bytecount]:
    grid[y][x] = '#'
  grid[0][0] = 'O'
  return solve(grid)

# Binary search for the first non-solveable grid.
lb = 0
ub = len(hits)
# Trivially solveable at 0, assume not solvable at len(hits).
while lb != ub:
  nb = (lb+ub)//2
  result = tryat(nb)
  resultstr = 'ok' if result else 'fail'
  print(f'solution in [{lb},{ub}]. trying at {nb} ({resultstr})')
  if result:
    # Solveable at nb, so answer is at least nb+1.
    lb = nb+1
  else:
    # Not solveable at nb, so answer is at most ub.
    ub = nb
print(f'not solveable after {lb} bytes: {hits[lb-1]}')
