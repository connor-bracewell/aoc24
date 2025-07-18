import sys
import re

with open(sys.argv[1]) as f:
  a = int(re.fullmatch(R'Register A: (-?\d+)\n', f.readline()).group(1))
  b = int(re.fullmatch(R'Register B: (-?\d+)\n', f.readline()).group(1))
  c = int(re.fullmatch(R'Register C: (-?\d+)\n', f.readline()).group(1))
  f.readline()
  ops = [int(c) for c in re.fullmatch(R'Program: ([\d,]+)\n',f.readline()).group(1).split(',')]
print(f'a={a} b={b} c={c}')
print(f'ops={ops}')

pc = 0
out = []
while pc >= 0 and pc < len(ops):
  ist = ops[pc]
  lop = ops[pc+1]
  match lop:
    case 4:
      cop = a
    case 5:
      cop = b
    case 6:
      cop = c
    case _:
      cop = lop
  match ist:
    case 0:
      # division by 2^cop is the same as shift right by cop.
      a = a>>cop
      print(f'adv {lop}({cop}); a={a}')
    case 1:
      b ^= lop
      print(f'bxl {lop}; b={b}')
    case 2:
      b = cop%8
      print(f'bst {lop}({cop}); b={b}')
    case 3:
      if a != 0:
        pc = lop
        print(f'jnz {lop}')
        continue
      print(f'jnz (pass)')
    case 4:
      b ^= c
      print(f'bxc c{c}; b={b}')
    case 5:
      out.append(cop%8)
      print(f'out {cop%8}')
    case 6:
      b = a>>cop
      print(f'bdv {lop}({cop}); b={b}')
    case 7:
      c = a>>cop
      print(f'cdv {lop}({cop}); c={c}')
  pc += 2 
print(','.join(map(lambda o: str(o), out)))
