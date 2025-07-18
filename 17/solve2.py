seq = [0,3,5,5,1,4,5,1,3,0,5,7,3,1,4,2]

def recursive(a, rem):
  if not rem: return a  # done!
  a <<= 3
  for d in range(8):
    a = a&(~0b111)|d  # replace the bottom 3 bits of a with d.
    out = a^0b110^(a>>(d^0b011))  # see notes.txt
    # print(f'trying {d:3b}, a is {a:b}, out is {out%8:b}')
    if out%8 == rem[0]:
      # print(f'match @ a={a} rem={rem}...')
      if (result := recursive(a, rem[1:])) is not None:
        return result
  # print('backing up...')
  return None

print(recursive(0, seq))
