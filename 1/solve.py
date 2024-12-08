import sys

list_l = []
list_r = []
with open(sys.argv[1]) as f:
  for line in f:
    print(line)
    l, r = line.split()
    list_l.append(int(l))
    list_r.append(int(r))

result = 0
list_l.sort()
list_r.sort()
for l,r in zip(list_l, list_r):
  result += abs(l-r)
print(result)
