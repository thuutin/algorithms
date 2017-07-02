from collections import deque
import sys


# sys.stdin = file("/Users/tin/Downloads/D-small-practice.in")

class Range():
  def __init__(self, a, b):
    self.a = a
    self.b = b
    self.e = b - a + 1

  def __str__(self):
    return str((self.a, self.b))

  def __len__(self):
    return self.b - self.a + 1

  def intersect(self, other):
    if self.b <= other.b:
      if self.a <= other.a:
        return self.b - other.a + 1
      else:
        return len(self)
    else:
      return other.intersect(self)


left = []
right = []


def merge(cache, these):
  if len(these) == 0:
    return []
  if len(these) == 1:
    return these
  i = 1
  stack = deque([these[0]])
  while i < len(these):
    next = these[i]
    if next.a > stack[0].b:
      stack.appendleft(next)
    elif next.b > stack[0].b:
      stack[0] = Range(stack[0].a, next.b)
    i += 1
  return stack


def solveIt(intervals):
  left = []
  right = []
  intervals = sorted(intervals, key=lambda x: x.a)
  mm = None
  for i in xrange(len(intervals)):
    now = intervals[i]
    remaining = intervals[:i]
    remaining.extend(intervals[i + 1:])
    merged = merge(None, remaining)
    intersect = 0
    for m in merged:
      intersect += len(m)
    if mm is None or mm > intersect:
      mm = intersect
  return mm
  pass


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    N, L1, R1, A, B, C1, C2, M = map(int, raw_input().split(" "))
    ranges = [Range(L1, R1)]
    prevX = L1
    prevY = R1
    for i in xrange(N - 1):
      x = (A * prevX + B * prevY + C1) % M
      y = (A * prevY + B * prevX + C2) % M
      prevX = x
      prevY = y
      ranges.append(Range(min(x, y), max(x, y)))
    print "Case #" + str(t) + ": " + str(solveIt(ranges))
