import sys

with open(sys.argv[1]) as f:
  result = 0
  grid = []
  for line in f:
    row = []
    for char in line.strip():
      row.append(char)
    grid.append(row)
  def printgrid(grid):
    for row in grid:
      for char in row:
        print(char, end='')
      print('')
  def find(row):
    result = 0
    for (x,m,a,s) in zip(row, row[1:], row[2:], row[3:]):
      if x == 'X' and m == 'M' and a == 'A' and s == 'S':
        result += 1
    return result
  def fliph(row):
    return row[::-1]
  for row in grid:
    result += find(row)
    result += find(fliph(row))
  printgrid(grid)
  print(result, ' horizontal')
  def transpose(grid):
    result = []
    for row in grid:
      for i, char in enumerate(row):
        if i+1 > len(result):
          result.append([])
        result[i].append(char)
    return result
  for row in transpose(grid):
    result += find(row)
    result += find(fliph(row))
  printgrid(transpose(grid))
  print(result, ' horizontal+vertical')
  def lshift(grid):
    result = []
    for i, row in enumerate(grid):
      result.append(['*' for _ in range(i)] + row)
    return result
  def rshift(grid):
    result = []
    for i, row in enumerate(grid):
      result.append(['*' for _ in range(len(row)-i-1)] + row)
    return result
  for row in transpose(lshift(grid)):
    result += find(row)
    result += find(fliph(row))
  printgrid(transpose(lshift(grid)))
  print(result, ' horizontal+vertical+updiag') 
  for row in transpose(rshift(grid)):
    result += find(row)
    result += find(fliph(row))
  printgrid(transpose(rshift(grid)))
  print(result)
