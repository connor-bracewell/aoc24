import sys
import random
import time

w = int(sys.argv[1])
h = int(sys.argv[2])
t = 1.0 / int(sys.argv[3])

rpx = 1+random.randrange(w-2)
rpy = 1+random.randrange(h-2)

cmap = {
  '#':['#','#'],
  'O':['[',']'],
  '.':['.','.'],
  '@':['@','.'],
}
grid = []
for y in range(h):
  row = ['#']
  for x in range(w-2):
    c = random.choices('#.O', weights=[1,7,2])[0]
    if y == 0 or y == h-1:
      c = '#'
    elif x == rpx-1 and y == rpy:
      c = '@'
    row.extend(cmap[c])
  row.append('#')
  grid.append(row)

def show():
  def color(text, ccode):
    return f'\033[{ccode}m{text}\033[0m'
  print('\n'.join(''.join(row) for row in grid).replace('.',' ').replace('[]',color('[]', 90)).replace('@',color('&',31)))
  print(f'\033[{h}F', end='')


rx=2*rpx-1
ry=rpy

def do_move(m):
  global rx, ry
  dx = 0
  dy = 0
  if m == '^':
    dy = -1
  elif m == '>':
    dx = 1
  elif m == 'v':
    dy = 1
  else: # <
    dx = -1
  if dx != 0:
    # horizontal move (simple)
    tx = rx+dx
    while grid[ry][tx] not in '#.':
      tx += dx
    if grid[ry][tx] == '.':
      while tx != rx:
        grid[ry][tx] = grid[ry][tx-dx]
        tx -= dx
      grid[ry][rx] = '.'
      rx = rx+dx
      return True
  else:
    # vertical move (complicated!)
    def cast(x,y,dy):
      # if true, tile (x,y) can move dy
      c = grid[y][x]
      if c in '.{}':
        return True
      if c == '[':
        grid[y][x] = '{'
        grid[y][x+1] = '}'
        if cast(x,y+dy,dy) and cast(x+1,y+dy,dy):
          return True
      elif c == ']':
        grid[y][x] = '}'
        grid[y][x-1] = '{'
        if cast(x,y+dy,dy) and cast(x-1,y+dy,dy):
          return True
      elif c == '@':
        return cast(x,y+dy,dy)
      return False  # us or child hit a wall
    def revert(x,y,dy):
      # cast failed; clean up markers
      c = grid[y][x]
      if c == '{':
        grid[y][x] = '['
        grid[y][x+1] = ']'
        revert(x,  y+dy,dy)
        revert(x+1,y+dy,dy)
      elif c == '}':
        grid[y][x] = ']'
        grid[y][x-1] = '['
        revert(x,  y+dy,dy)
        revert(x-1,y+dy,dy)
    def commit(x,y,dy):
      # move children, then yourself
      c = grid[y][x]
      if c == '.':
        return
      if c == '{':
        commit(x,y+dy,dy)
        commit(x+1,y+dy,dy)
        grid[y+dy][x] = '['
        grid[y+dy][x+1] = ']'
        grid[y][x] = '.'
        grid[y][x+1] = '.'
        return
      if c == '}':
        commit(x,y+dy,dy)
        commit(x-1,y+dy,dy)
        grid[y+dy][x] = ']'
        grid[y+dy][x-1] = '['
        grid[y][x] = '.'
        grid[y][x-1] = '.'
        return
    if cast(rx,ry,dy):
      commit(rx,ry+dy,dy)
      grid[ry][rx] = '.'
      ry = ry+dy
      grid[ry][rx] = '@'
      return True
    else:
      revert(rx,ry+dy,dy)
  return False

try:
  moves = list('<>^v')
  random.shuffle(moves)
  while True:
    show()
    time.sleep(t)
    if random.random() < 0.25:
      random.shuffle(moves)
    if do_move(moves[0]):
      continue
    for move in moves[1:]:
      if do_move(move): 
        random.shuffle(moves)
        moves = [move] + [other for other in moves if other != move] 
        break
    else:
      print('\n'*h + 'stuck!')
      break
except KeyboardInterrupt:
  print('\n'*h)
