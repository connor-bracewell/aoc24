seq = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]

# given the leading bits of `a` and the remaining output,
# return the least continuation of `a` that generates that output,
# or None if no such continuation exists.
def recursive(a, rem):
  if not rem:
    # No more output to generate!
    return a
  # Try each possible value for the next 3 bits, least first.
  for d in range(8):
    ap = (a<<3)|d
    # See notes.txt for the reasoning.
    b = ap^0b110
    c = ap>>(d^0b011)
    out = (b^c)%8
    if out == rem[-1]:
      # (a<<3)|d outputs the expected digit. See if there
      # is a continuation that generates the remaining output.
      if (result := recursive(ap, rem[:-1])) is not None:
        return result
  return None

print(recursive(0, seq))
