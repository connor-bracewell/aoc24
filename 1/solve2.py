import sys

list_l = []
count_r = {}
with open(sys.argv[1]) as f:
  for line in f:
    l_str, r_str = line.split()
    list_l.append(int(l_str))
    r = int(r_str)
    if r not in count_r:
      count_r[r] = 0
    count_r[r] += 1

result = 0
for l in list_l:
  if l in count_r:
    result += l * count_r[l]
print(result)
