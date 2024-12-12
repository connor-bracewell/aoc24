import sys

with open(sys.argv[1]) as f:
  grid = [[c for c in line.strip()] for line in f]
visited =[[False for _ in row] for row in grid]
def explore(y,x):
  visited[y][x] = True
  c = grid[y][x]
  area = 1
  perim = 0
  if x==0 or grid[y][x-1] != c:
    perim += 1
  elif not visited[y][x-1]:
    res = explore(y,x-1)
    area += res[0]
    perim += res[1]
  if x==len(grid[0])-1 or grid[y][x+1] != c:
    perim += 1
  elif not visited[y][x+1]:
    res = explore(y,x+1)
    area += res[0]
    perim += res[1]
  if y==0 or grid[y-1][x] != c:
    perim += 1
  elif not visited[y-1][x]:
    res = explore(y-1,x)
    area += res[0]
    perim += res[1]
  if y==len(grid)-1 or grid[y+1][x] != c:
    perim += 1
  elif not visited[y+1][x]:
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
    print(f'area at {y},{x} a={res[0]} p={res[1]}')
    result += res[0]*res[1]
print(f'{result}')
