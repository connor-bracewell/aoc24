import sys

charize = lambda n: 'wubrg'[n]

towels = []
patterns = []
with open(sys.argv[1]) as f:
  lookup = {charize(n): n for n in range(5)}
  intize = lambda c: lookup[c]
  for s in f.readline().strip().split(', '):
    towels.append(list(map(intize, s)))
  f.readline()
  for l in f:
    patterns.append(list(map(intize, l.strip())))

# Trie node: children 0-4, is_terminal 5, str 6
trie = [None]*7
trie[6] = ''
for towel in towels:
  node = trie
  for n in towel:
    if node[n] is None:
       node[n] = [None]*7
       node[n][6] = node[6].strip('*')+charize(n)
    node = node[n]
  if not node[5]:
    node[5] = True
    node[6] += '*'

def solve(pattern):
  print(f'Trying pattern: {''.join(map(charize, pattern))}')
  # Start with a single prefix match (the empty string).
  queue = [(trie, 1)]
  for i, n in enumerate(pattern):
    nqueue = []
    loopsum = 0
    for node, nodesum in queue:
      if node[n] is not None:
        print(f'matched {charize(n)} ({i}) at {node[n][6]}')
        nqueue.append((node[n], nodesum))
        if node[n][5]:
          # When we hit a terminal, add its prefix match count to the
          # prefix count for the subsequent empty string prefix.
          loopsum += nodesum
    if loopsum:
      nqueue.append((trie, loopsum))
    queue = nqueue
  print(f'Pattern has {loopsum} options.')
  return loopsum

result = 0
for pattern in patterns:
  result += solve(pattern)
print(f'{result}')
