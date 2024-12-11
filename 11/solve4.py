import sys
from math import log10

with open(sys.argv[1]) as f:
  init = [int(s) for s in f.readline().split()]
reps = int(sys.argv[2]) if len(sys.argv) > 2 else 75

childcache = {0: [1]}
def children(n):
  if n not in childcache:
    digits = int(log10(n))+1
    if digits % 2 == 0:
      half = 10**(digits//2)
      childcache[n] = [n//half, n%half]
    else:
      childcache[n] = [n*2024]
  return childcache[n]

def addn(d,l,c):
  for i in l:
    if i not in d:
      d[i] = 0
    d[i] += c

stones = {}
addn(stones,init,1)
for it in range(reps):
  nstones = {}
  for n,count in stones.items():
    addn(nstones, children(n), count)
  stones = nstones
print(sum([count for n,count in stones.items()]))
