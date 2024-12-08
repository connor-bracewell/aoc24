import sys

with open(sys.argv[1]) as f:
  result = 0
  for line in f:
    numbers = line.split()
    target = int(numbers[0][:-1])
    #print(f'target: {target}')
    inputs = [int(n) for n in numbers[1:]]
    #print(f'inputs: {inputs}')
    mins = [inputs[0]]
    maxs = [inputs[0]]
    for i,n in enumerate(inputs[1:]):
      mins.append(mins[i] if n == 1 else mins[i]+n) 
      maxs.append(int(str(maxs[i])+str(n))) 
    #print(f'mins: {mins}')
    #print(f'maxs: {maxs}')
    if target == mins[-1] or target == maxs[-1]:
      #print(f'{target} is min({mins[-1]}) or max({maxs[-1]})')
      result += target
      continue
    if target < mins[-1] or target > maxs[-1]:
      #print(f'{target} is outside of [{mins[-1]},{maxs[-1]}]')
      continue
    partials = {inputs[0]}
    #print(f'after {inputs[0]}: {partials}')
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
      #print(f'after {n}: {partials}')
    if target in partials:
      #print(f'{target} in {partials}')
      result += target
  print(f'{result}')
