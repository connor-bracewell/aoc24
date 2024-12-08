import sys

with open(sys.argv[1]) as f:
  result = 0
  for line in f:
    seq = [int(s) for s in line.split()]
    safe = True
    for a,b,c in zip(seq, seq[1:], seq[2:]):
      if abs(a-b) == 0 or abs(a-b) > 3 or abs(b-c) == 0 or abs(b-c) > 3 or (a-b>0) != (b-c>0):
        print(f"Bad chain: {a} {b} {c}")
        safe = False
        break
    if safe:
      result += 1
  print(result)
