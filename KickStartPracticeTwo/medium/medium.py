import math
from collections import deque


def solveIt(N):
  if N == 1:
    return 2

  n = 60
  while n > 0:
    L = 2
    R = N
    while L < R:
      if R - L <= 3:
        for i in xrange(L, R + 1):
          if i ** (n + 1) - 1 == N * (i - 1):
            return (i, n)

      mid = (L + R) / 2
      left = mid ** (n + 1) - 1
      right = (mid - 1) * N
      if left > right:
        R = mid - 1
      elif left < right:
        L = mid + 1
      else:
        return (mid, n)

    n -= 1


solveIt(24)
if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    it = int(raw_input(), 10)
    r = solveIt(it)
    print "Case #" + str(t) + ": " + str(r[0])
  pass
