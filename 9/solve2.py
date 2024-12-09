import sys

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  pos = 0 # current 'filesystem' position
  natpos = [] # natural 'filesystem' position for file n
  gaps = [] # positions (sorted) of gaps of size n
  for i,c in enumerate(line):
    n = int(c)
    if i%2 == 0:
      # a file; record its natural position
      natpos.append(pos)
    elif n != 0:
      # a gap; record it in the lookup
      while n+1 > len(gaps):
        gaps.append([])
      gaps[n].append(pos)
    pos += n
  #print(f'gaps: {gaps}')

  idx = len(line)//2
  def getbest(n, gaps):
    best = None
    while n < len(gaps):
      if len(gaps[n]) > 0 and ((best is None) or (gaps[n][0] < gaps[best][0])):
        best = n
      n += 1
    return best
  result = 0
  while idx >= 0:
    n = int(line[idx*2]) 
    pos = natpos[idx]
    bestgap = getbest(n, gaps)
    if bestgap is None or gaps[bestgap][0] > pos:
      #print(f'leaving {idx} at {pos}') 
      pass
    else: 
      bestpos = gaps[bestgap][0]
      #print(f'moving {idx} from {pos} to {bestpos}')
      pos = bestpos
      gaps[bestgap] = gaps[bestgap][1:]
      newpos = bestpos+n
      newgap = bestgap-n
      if newgap != 0:
        i = 0
        newlist = []
        while i < len(gaps[newgap]) and gaps[newgap][i] < newpos:
          newlist.append(gaps[newgap][i])
          i += 1
        newlist.append(newpos)
        newlist += gaps[newgap][i:]
        gaps[newgap] = newlist
      #print(f'gaps now: {gaps}')
    for _ in range(n):
      result += pos*idx
      pos += 1
    idx -= 1
  print(f'{result}')
