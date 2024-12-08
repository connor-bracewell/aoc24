import sys

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
    disallowed = set()
    for n in numbers:
      if n in disallowed:
        print(f'{numbers} bad; {n} disallowed here')
        break
      if n in rules:
        disallowed.update(rules[n])
    else:
      mid = numbers[len(numbers)//2]
      print(f'{numbers} good; adding {mid}')
      result += mid
  print(f'{result}')
