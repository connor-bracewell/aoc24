import sys

with open(sys.argv[1]) as f:
  result = 0
  grid = []
  for line in f:
    row = []
    for char in line.strip():
      row.append(char)
    grid.append(row)
  for y in range(1, len(grid)-1):
    for x in range(1, len(grid[y])-1):
      if grid[y][x] != 'A':
        continue
      # Check the up-left diagonal.
      if not (grid[y-1][x-1] in ['M','S'] and grid[y+1][x+1] in ['M','S'] and grid[y-1][x-1] != grid[y+1][x+1]):
        continue
      # Check the up-right diagonal.
      if not (grid[y-1][x+1] in ['M','S'] and grid[y+1][x-1] in ['M','S'] and grid[y-1][x+1] != grid[y+1][x-1]):
        continue
      result += 1 
  print(result)
