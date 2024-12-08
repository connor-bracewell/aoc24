import sys

with open(sys.argv[1]) as f:
  result = 0
  for line in f:
    numbers = line.split()
    target = int(numbers[0][:-1])
    print(f'target: {target}')
    inputs = [int(n) for n in numbers[1:]]
    print(f'inputs: {inputs}')
    partials = {inputs[0]}
    print(f'after {inputs[0]}: {partials}')
    for n in inputs[1:]:
      new_partials = set()
      for m in partials:
        if m+n <= target:
          new_partials.add(m+n)
        if m*n <= target:
          new_partials.add(m*n)
        cat = int(str(m)+str(n))
        if cat <= target:
          new_partials.add(cat)
      partials = new_partials
      print(f'after {n}: {partials}')
    if target in partials:
      print(f'{target} in {partials}')
      result += target
  print(f'{result}')
