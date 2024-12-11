import sys
from math import log10

reps = int(sys.argv[2])
cache = [{} for _ in range(reps+1)]

def lookup(times, n):
  if n not in cache[times]:
    cache[times][n] = compute(times, n)
  return cache[times][n]

def compute(times, n):
  if times == 0:
    return 1
  if n == 0:
    return lookup(times-1, 1)
  digits = int(log10(n))+1
  if digits % 2 != 0:
    return lookup(times-1, n*2024)
  split = 10**(digits//2)
  return lookup(times-1, n//split) + lookup(times-1, n%split)

with open(sys.argv[1]) as f:
  stones = [int(s) for s in f.readline().split()]
result = sum([lookup(reps, s) for s in stones])
if reps < 10:
  for i,table in enumerate(cache[1:]):
    print(f'cache {i+1}: {table}')
print(result)
