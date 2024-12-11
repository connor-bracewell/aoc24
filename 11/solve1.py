import sys
from math import log10

with open(sys.argv[1]) as f:
  stones = [int(s) for s in f.readline().split()]
reps = int(sys.argv[2])
for i in range(reps):
  new = []
  for stone in stones:
    if stone == 0:
      new.append(1)
      continue
    digits = int(log10(stone))+1
    if digits % 2 != 0:
      new.append(stone*2024)
      continue
    split = 10**(digits//2)
    new.append(stone//split)
    new.append(stone%split)
  print(i)
  stones = new
print(len(stones))
