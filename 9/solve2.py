import sys

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  pos = 0 # current 'filesystem' position
  natpos = [] # natural 'filesystem' position for file n
  gaps = [] # positions (sorted) of gaps of size n
  for i,c in enumerate(line):
    n = int(c)
    if i%2 == 0:
      natpos.append(pos)
    elif n != 0:
      while n+1 > len(gaps):
        gaps.append([])
      gaps[n].append(pos)
    pos += n
  #print(f'gaps: {gaps}')

  tail = len(line)-1
  if tail%2 == 1:
    tail -= 1
  def getbest(n, gaps):
    best = None
    while n < len(gaps):
      if len(gaps[n]) > 0 and ((best is None) or (gaps[n][0] < gaps[best][0])):
        best = n
      n += 1
    return best
  result = 0
  while tail >= 0:
    
    n = int(line[tail]) 
    pos = natpos[tail//2]
    bestgap = getbest(n, gaps)
    if bestgap is None or gaps[bestgap][0] > pos:
      #print(f'leaving {tail//2} at {pos}') 
      pass
    else: 
      bestpos = gaps[bestgap][0]
      #print(f'moving {tail//2} from {pos} to {bestpos}')
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
      result += pos*(tail//2)
      pos += 1
    tail -= 2
  print(f'{result}')
