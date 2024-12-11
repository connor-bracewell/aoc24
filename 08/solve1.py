import sys

with open(sys.argv[1]) as f:
  ants = {}
  for y,line in enumerate(f):
    for x,c in enumerate(line.strip()):
      if c != '.':
        if c not in ants:
          ants[c] = []
        ants[c].append((x,y))
  def in_bounds(pos):
    result = (0 <= pos[0] <= y and 0 <= pos[1] <= x)
    #print(f'{pos} {"is" if result else "isn\'t"} in bounds ({y}x{x})')
    return result
  nodes = set()
  for c,locs in ants.items():
    for i,loc1 in enumerate(locs):
      for loc2 in locs[i+1:]:
        node1 = (2*loc1[0] - loc2[0],2* loc1[1] - loc2[1])
        if in_bounds(node1):
          nodes.add(node1)
        node2 = (2*loc2[0] - loc1[0],2* loc2[1] - loc1[1])
        if in_bounds(node2):
          nodes.add(node2)
  print(f'{len(nodes)}')
