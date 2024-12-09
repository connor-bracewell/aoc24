import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  pos = 0
  natpos = []
  gaps = []
  for i,c in enumerate(line):
    n = int(c)
    if i%2 == 0:
      natpos.append(pos)
    elif n != 0:
      while n+1 > len(gaps):
        gaps.append([])
      gaps[n].append(pos)
    pos += n
  print(f'gaps: {gaps}')
  outline = ['[....]' for _ in range(pos)]

  tail = len(line) #-1
  if tail%2 == 1:
    tail -= 1
  def getbest(n, gaps):
    ogn = n
    best = None
    while n < len(gaps):
      if len(gaps[n]) > 0 and ((best is None) or (gaps[n][0] < gaps[best][0])):
        best = n
      elif ogn == 1 and len(gaps[n]) == 0:
        print(f'skipping gaps[{n}] (no entries)')
      elif ogn == 1:
        print(f'gaps[{n}][0] = {gaps[n][0]}, worse than best {best}')
      n += 1
    return best
  result = 0
  while tail >= 0:
    n = int(line[tail]) 
    nat = natpos[tail//2]
    pos = None
    bestgap = getbest(n, gaps)
    if bestgap is not None:
      bestpos = gaps[bestgap][0]
      if bestpos < nat:
        #print(f'moving {tail//2} from {nat} to {bestpos}')
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
      elif n == 1:
        print(f'no better gap of size 1 for index {tail//2} (nat is {nat}, best is size {bestgap})')
        for i,l in enumerate(gaps):
          print(f'gaps {i}: {l}')
    elif n == 1:
      print(f'no gaps of size 1 for index {tail//2}')
    if pos is None:
      #print(f'leaving {tail//2} at {nat}') 
      pos = nat
    temp = 0
    for _ in range(n):
      if outline[pos] != '[....]':
        print(f'bad write at {pos}')
      outline[pos] = f'[{(tail//2):4}]'
      temp += pos*(tail//2)
      pos += 1
    #print(f'adding {temp} for idx {tail//2}')
    result += temp
    tail -= 2
  print(''.join(outline))
  print(f'{result}')
