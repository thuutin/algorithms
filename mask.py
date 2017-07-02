
import sys
LEN = 27


def solve(a):
  result = [1] * 27
  arr = map(bin, a)
  newMore = arr
  flipped = set(range(-27, 0))
  for i in xrange(len(result)):
    flipped.remove(i - LEN)
    yes = True
    for m in newMore:
      satisfied = False
      for f in flipped:
        if len(m) - 2 > (f * -1) - 1 >= 0 and m[f] == '1':
          satisfied = True
          break
      if satisfied:
        continue
      else:
        yes = False
        break
    if not yes:
      flipped.add(i - LEN)
    else:
      result[i] = 0

  it = "".join(map(str, result))
  return int(it, 2)
# n = int(.strip())
a = map(int, "1 2 4 8 16 32 64 256 512 128".strip().split(' '))
a = map(int, "7 14 28".strip().split(' '))
result = solve(a)
print result