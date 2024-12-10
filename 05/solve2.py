import sys
from functools import cmp_to_key

with open(sys.argv[1]) as f:
  # a in rules[b] implies a cannot come after b.
  rules = {}
  for line in f:
    if len(line) == 1:
      break
    [a, b] = [int(n) for n in line.split('|')]
    if b not in rules:
      rules[b] = []
    rules[b].append(a)
  result = 0
  for line in f:
    if len(line) == 0:
      break
    numbers = [int(n) for n in line.split(',')]
    cmp = lambda a,b: -1 if (b in rules and a in rules[b]) else 1 if (a in rules and b in rules[a]) else 0
    fixed = sorted(numbers, key=cmp_to_key(cmp))
    if numbers != fixed:
      mid = fixed[len(fixed)//2]
      print(f'reordered {numbers}')
      print(f'       to {fixed}; adding {mid}')
      result += mid
  print(f'{result}')
