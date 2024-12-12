import sys

with open(sys.argv[1]) as f:
  grid = [[c for c in line.strip()] for line in f]
visited =[[None for _ in row] for row in grid]
def iny(y):
  return 0<=y<len(grid)
def inx(x):
  return 0<=x<len(grid[0])
def explore(y,x):
  visited[y][x] = [False,False,False,False]  # w,e,n,s
  c = grid[y][x]
  area = 1
  perim = 0
  if x==0 or grid[y][x-1] != c:
    visited[y][x][0] = True
    seen = 0
    if iny(y-1) and grid[y-1][x] == c and visited[y-1][x] and visited[y-1][x][0]:
      seen += 1
    if iny(y+1) and grid[y+1][x] == c and visited[y+1][x] and visited[y+1][x][0]:
      seen +=1
    if seen == 2:
      perim -= 1
    elif seen == 0:
      if c == 'R': print(f'new edge west of {c} at {y},{x}')
      perim += 1
  if x==len(grid[0])-1 or grid[y][x+1] != c:
    visited[y][x][1] = True
    seen = 0
    if iny(y-1) and grid[y-1][x] == c and visited[y-1][x] and visited[y-1][x][1]:
      seen += 1
    if iny(y+1) and grid[y+1][x] == c and visited[y+1][x] and visited[y+1][x][1]:
      seen += 1
    if seen == 2:
      perim -= 1
    elif seen == 0:
      if c == 'R': print(f'new edge east of {c} at {y},{x}')
      perim += 1
  if y==0 or grid[y-1][x] != c:
    visited[y][x][2] = True
    seen = 0
    if inx(x-1) and grid[y][x-1] == c and visited[y][x-1] and visited[y][x-1][2]:
      seen += 1
    if inx(x+1) and grid[y][x+1] == c and visited[y][x+1] and visited[y][x+1][2]:
      seen += 1
    if seen == 2:
      perim -= 1
    elif seen == 0:
      if c == 'R': print(f'new edge north of {c} at {y},{x}')
      perim += 1
  if y==len(grid)-1 or grid[y+1][x] != c:
    visited[y][x][3] = True 
    seen = 0
    if inx(x-1) and grid[y][x-1] == c and visited[y][x-1] and visited[y][x-1][3]:
      seen += 1
    if inx(x+1) and grid[y][x+1] == c and visited[y][x+1] and visited[y][x+1][3]:
      seen += 1
    if seen == 2:
      perim -= 1
    elif seen == 0:
      if c == 'R': print(f'new edge south of {c} at {y},{x}')
      perim += 1
  if (not visited[y][x][0]) and not visited[y][x-1]:
    res = explore(y,x-1)
    area += res[0]
    perim += res[1]
  if (not visited[y][x][1]) and not visited[y][x+1]:
    res = explore(y,x+1)
    area += res[0]
    perim += res[1]
  if (not visited[y][x][2]) and not visited[y-1][x]:
    res = explore(y-1,x)
    area += res[0]
    perim += res[1]
  if (not visited[y][x][3]) and not visited[y+1][x]:
    res = explore(y+1,x)
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
