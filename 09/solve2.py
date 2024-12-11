import sys
from bisect import insort

with open(sys.argv[1]) as f:
  line = f.readline().strip()
files = []
gaps = [] # positions (sorted) of gaps of size n
pos = 0 # current 'filesystem' position
for i,n in enumerate([int(c) for c in line]):
  if i%2 == 0:
    files.append((pos,n))
  elif n != 0:
    while len(gaps) <= n:
      gaps.append([])
    gaps[n].append(pos)
  pos += n
print(f'gaps: {gaps}')

def getbestgap(n, gaps):
  bestgap = None
  bestpos = None
  for i,l in enumerate(gaps[n:]):
    if len(l) > 0 and (bestgap is None or l[0] < bestpos):
      bestgap = i
      bestpos = l[0]
  return n+bestgap

result = 0
for idx,pos,n in reversed([(i,file[0],file[1]) for i,file in enumerate(files)]):
  bestgap = getbestgap(n, gaps)
  if bestgap is None or gaps[bestgap][0] > pos:
    print(f'leaving {idx} (len {n}) at {pos}') 
    pass
  else: 
    bestpos = gaps[bestgap].pop(0)
    print(f'moving {idx} (len {n}) from {pos} to {bestpos} (gap of size {bestgap})')
    pos = bestpos
    if (newgap := bestgap-n) != 0:
      insort(gaps[newgap], bestpos+n)
    #print(f'gaps now: {gaps}')
  result += idx * ((pos+n-1)*(pos+n) - (pos-1)*pos) // 2
print(f'{result}')
