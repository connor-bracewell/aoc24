import sys
from math import log10

reps = int(sys.argv[2]) if len(sys.argv) > 2 else 75

childcache = {0: [1]}
valcache = [{} for _ in range(reps+1)]

def children(n):
  if n not in childcache:
    digits = int(log10(n))+1
    if digits % 2 == 0:
      half = 10**(digits//2)
      childcache[n] = [n//half, n%half]
    else:
      childcache[n] = [n*2024]
  return childcache[n]

with open(sys.argv[1]) as f:
  init = [int(s) for s in f.readline().split()]

todo = set(init)
for it in range(reps+1):
  ntodo = set()
  for n in todo:
    valcache[it][n] = None
    ntodo.update(children(n))
  todo = ntodo

for n in valcache[reps]:
  valcache[reps][n] = 1
for it in reversed(range(reps)):
  for n in valcache[it]:
    valcache[it][n] = sum([valcache[it+1][c] for c in childcache[n]])

result = sum([valcache[0][n] for n in init])
print(result)
