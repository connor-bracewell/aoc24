import sys

list_l,list_r = [],[]
with open(sys.argv[1]) as f:
  for line in f:
    print(line.strip())
    l,r = line.split()
    list_l.append(int(l))
    list_r.append(int(r))
print(sum([abs(l-r) for l,r in zip(sorted(list_l),sorted(list_r))]))
