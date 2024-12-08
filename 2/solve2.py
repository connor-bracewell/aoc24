import sys

def check(seq, skip=False):
  print(f"Trying sequence: {seq}")
  if len(seq) < 2:
    return True
  diff = seq[0] - seq[1]
  if diff == 0 or abs(diff) > 3:
    print(f"Bad starting pair {seq[0]} {seq[1]}")
    return False
  def check2(seq, skip, asc):
    for i in range(len(seq)-1):
      diff = seq[i] - seq[i+1]
      if diff == 0 or abs(diff) > 3 or (diff<0) != asc:
        if skip:
          skipped = [seq[i]] + seq[i+2:]
          print(f"Bad pair {seq[i]} {seq[i+1]}, trying continuation {skipped}")
          return check2(skipped, False, asc)
        else:
          print("Bad sequence")
          return False
    print("Good sequence")
    return True
  return check2(seq[1:], skip, diff < 0)

with open(sys.argv[1]) as f:
  result = 0
  for line in f:
    seq = [int(s) for s in line.split()]
    if check(seq, True) or check(seq[1:]) or check([seq[0]] + seq[2:]):
      result += 1
    print("===")
    # _ = input()
  print(result)
