import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

with open(sys.argv[1]) as f:
  ants = {}
  for y,line in enumerate(f):
    for x,c in enumerate(line.strip()):
      if c != '.':
        if c not in ants:
          ants[c] = []
        ants[c].append((x,y))
  def add(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])
  def sub(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1]) 
  def in_bounds(pos):
    result = (0 <= pos[0] <= y and 0 <= pos[1] <= x)
    logging.debug(f'{pos} {"is" if result else "isn\'t"} in bounds ({y}x{x})')
    return result
  nodes = set()
  for c,locs in ants.items():
    for i,loc1 in enumerate(locs):
      for loc2 in locs[i+1:]:
        loc = loc1
        delta = sub(loc1,loc2)
        while in_bounds(loc):
          nodes.add(loc)
          loc = add(loc, delta)
        loc = loc1
        while in_bounds(loc):
          nodes.add(loc)
          loc = sub(loc, delta)
  print(f'{len(nodes)}')
