import sys

sys.setrecursionlimit(1000000)
cache = {}
MOD = 1000000009


def numberOfLists(s, m, d, prev):
  if s < 0:
    return 0
  if s == 0:
    return 1
  if prev in cache:
    return cache[prev]
  big = min(s, m)
  small = 1
  choices = 0
  if prev != -1:
    prevMin = max(prev - d, 1)
    prevMax = min(prev + d, m)
    if big < prevMin:
      return 0
    small = prevMin
    big = min(prevMax, big)
  for i in xrange(small, big + 1):
    choices += numberOfLists(s - i, m, d, i) % MOD
    choices = choices % MOD
  if s >= m:
    cache[prev] = choices
  return choices


s = 100000
J = 1
while J < s:
  print J
  numberOfLists(J, 3, 2, -1)
  J += 2
print numberOfLists(1000000, 3, 2, -1)
