import sys

with open(sys.argv[1]) as f:
  grid = [[c for c in line.strip()] for line in f]
visited =[[None for _ in row] for row in grid]

def iny(y):
  return 0<=y<len(grid)
def inx(x):
  return 0<=x<len(grid[0])

dw,de,dn,ds = 0,1,2,3

def sample(y,x,d):
  if d == dw:
    return grid[y][x-1] if inx(x-1) else None
  if d == de:
    return grid[y][x+1] if inx(x+1) else None
  if d == dn:
    return grid[y-1][x] if iny(y-1) else None
  return grid[y+1][x] if iny(y+1) else None

def anyvisit(y,x,d):
  if d == dw:
    return inx(x-1) and visited[y][x-1]
  if d == de:
    return inx(x+1) and visited[y][x+1]
  if d == dn:
    return iny(y-1) and visited[y-1][x]
  return iny(y+1) and visited[y+1][x]

def samplev(y,x,d,d2):
  if d == dw:
    return inx(x-1) and visited[y][x-1] and visited[y][x-1][d2]
  if d == de:
    return inx(x+1) and visited[y][x+1] and visited[y][x+1][d2]
  if d == dn:
    return iny(y-1) and visited[y-1][x] and visited[y-1][x][d2]
  return iny(y+1) and visited[y+1][x] and visited[y+1][x][d2]

def rell(d):
  if d == dw:
    return dn
  if d == de:
    return ds
  if d == dn:
    return de
  return dw

def relr(d):
  if d == dw:
    return ds
  if d == de:
    return dn
  if d == dn:
    return dw
  return de

def adjresult(y,x,d,c):
  findl = sample(y,x,rell(d)) == c and samplev(y,x,rell(d),d)
  findr = sample(y,x,relr(d)) == c and samplev(y,x,relr(d),d)
  if findl and findr: return -1
  if findl or findr: return 0
  return 1

def explore3(y,x,d):
  if d == dw:
    return explore(y,x-1)
  if d == de:
    return explore(y,x+1)
  if d == dn:
    return explore(y-1,x)
  return explore(y+1,x)

# returns the unexplored [area,perimeter] of the region
# containing the unexplored point (y,x).
def explore(y,x):
  if visited[y][x]:
    return (0,0)
  # visited: is there a fence to the west/east/north/south of here
  visited[y][x] = [False,False,False,False]
  c = grid[y][x]
  area = 1
  perim = 0
  # for each direction, check if a fence is needed
  # and update perim appropriately
  conts = []
  for d in [dw,de,dn,ds]:
    if sample(y,x,d) != c:
      visited[y][x][d] = True
      perim += adjresult(y,x,d,c)
    else:
      conts.append(d)
  # for each adjacent square of the same type, explore again
  for d in conts:
    res = explore3(y,x,d)
    area += res[0]
    perim += res[1]
  return (area, perim)

result = 0
for y,row in enumerate(grid):
  for x,c in enumerate(row):
    if visited[y][x]:
      continue
    res = explore(y,x)
    print(f'area of {grid[y][x]} at {y},{x} a={res[0]} p={res[1]}')
    result += res[0]*res[1]
print(f'{result}')
