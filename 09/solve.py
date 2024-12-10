import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  outline = ''
  head = 0 # head pointer in line
  tail = len(line)-1 # tail pointer in line
  if tail % 2 == 1:
    tail -= 1
  tail_used = 0
  pos = 0 # position in system
  result = 0
  while head < tail: 
    print(f'writing original "{head//2}" x{line[head]} (head={head} tail={tail})')
    for i in range(int(line[head])):
      outline += str(head//2)
      print(f'adding {pos} * {head//2} = {pos*(head//2)}')
      result += pos*(head//2)
      pos += 1
    gap = int(line[head+1])
    while True:
      if tail_used == int(line[tail]):
        tail -= 2
        tail_used = 0
      if gap == 0:
        break
      outline += str(tail//2)
      print(f'adding {pos} * {tail//2} = {pos*(tail//2)}')
      result += pos*(tail//2)
      pos += 1
      gap -= 1
      tail_used += 1
    head += 2
    if head == tail:
      for _ in range(tail_used, int(line[tail])):
        print(f'{tail//2}', end='')
        print(f'adding {pos} * {tail//2} = {pos*(tail//2)}')
        result += pos*(tail//2)
        pos += 1 
  print(outline)
  print(f'{result}')
