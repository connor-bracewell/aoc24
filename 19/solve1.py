import sys

def intize(c):
  return {'w':0,'u':1,'b':2,'r':3,'g':4}[c]

def charize(n):
  return 'wubrg'[n]

with open(sys.argv[1]) as f:
  towels = []
  for s in f.readline().strip().split(', '):
    towels.append(list(map(intize, s)))
  f.readline()
  patterns = []
  for l in f:
    patterns.append(list(map(intize, l.strip())))

trie = [None]*7
for towel in towels:
  node = trie
  for i, n in enumerate(towel):
    if node[n] is None:
      node[n] = [None]*7
      node[n][6] = ''.join(map(charize, towel[:i+1]))
    node = node[n]
  if not node[5]:
    node[5] = True
    node[6] += '*'

def solve(pattern):
  print(f'Trying pattern: {''.join(map(charize, pattern))}')
  queue = [trie]
  nqueue = []
  looped = False
  for i, n in enumerate(pattern):
    looped = False
    for node in queue:
      if node[n] is not None:
        print(f'matched {charize(n)} ({i}) at {node[n][6]}')
        nqueue.append(node[n])
        if node[n][5] and not looped:
          nqueue.append(trie)
          looped = True
    queue = nqueue
    nqueue = []
  return looped

result = 0
for pattern in patterns:
  if solve(pattern):
    result += 1
print(f'{result}')
