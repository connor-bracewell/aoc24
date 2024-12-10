import logging
import sys
from math import ceil,log10

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

with open(sys.argv[1]) as f:
  result = 0
  for line in f:
    numbers = line.split()
    target = int(numbers[0][:-1])
    logging.debug(f'target: {target}')
    inputs = [int(n) for n in numbers[1:]]
    logging.debug(f'inputs: {inputs}') 
    mins = [inputs[0]]
    maxs = [inputs[0]]
    for i,n in enumerate(inputs[1:]):
      mins.append(mins[i]*n if (mins[i] == 1 or n == 1) else mins[i]+n) 
      maxs.append(maxs[i]*(10**ceil(log10(n+1))) + n) 
    logging.debug(f'  mins: {mins}')
    logging.debug(f'  maxs: {maxs}')
    if target == mins[-1] or target == maxs[-1]:
      logging.debug(f'{target} is min({mins[-1]}) or max({maxs[-1]})')
      result += target
      continue
    if target < mins[-1] or target > maxs[-1]:
      logging.debug(f'{target} is outside of [{mins[-1]},{maxs[-1]}]')
      continue
    targets = {target}
    for i,n in enumerate(inputs[:0:-1]):
      if not targets:
        logging.debug('no remaining targets')
        break
      logging.debug(f'using {inputs[:-i] if i != 0 else inputs} to reach {targets}')
      ndigits = 10**ceil(log10(n+1))
      new_targets = set()
      for t in targets:
        if t < mins[-i-1] or t > maxs[-i-1]:
          logging.debug(f'{t} outside current min/max ({mins[-1-i]}/{maxs[-1-i]})')
          continue
        if t % ndigits == n and t != n:
          # inverse concat
          new_targets.add(t//ndigits)
        if t % n == 0:
          new_targets.add(t//n)
        new_targets.add(t-n)
      targets = new_targets
    else:
      found = (inputs[0] in targets)
      verb = 'is' if found else 'isn\'t'
      logging.debug(f'{inputs[0]} {verb} in final targets {targets}')
      if found:
        result += target
  print(f'{result}')
