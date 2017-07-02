def solve(arr):
  pairCount = {}
  thatOne = None
  meetRowHavingOneStar = False
  for i in xrange(len(arr)):
    r = arr[i]
    trueCount = 0
    true = []
    that = None
    for j in xrange(len(r)):
      if r[j]:
        that = j
        true.append(j)
        trueCount += 1
    if trueCount == 1:
      if not meetRowHavingOneStar:
        thatOne = (i, that)
        meetRowHavingOneStar = True
      else:
        return "IMPOSSIBLE"
    elif trueCount != 2:
      return "IMPOSSIBLE"
    else:
      if (true[0], true[1]) in pairCount:
        pairCount[(true[0], true[1])] += 1
      else:
        pairCount[(true[0], true[1])] = 1

  for pp in pairCount.itervalues():
    if pp != 2:
      return "IMPOSSIBLE"
  if not meetRowHavingOneStar:
    return "IMPOSSIBLE"

  meetColHavingOneStar = False

  for i in xrange(len(arr)):
    trueCount = 0
    that = None
    for j in xrange(len(arr)):
      if arr[j][i]:
        that = j
        trueCount += 1
    if trueCount == 1:
      if not meetColHavingOneStar:
        if thatOne[0] != that or thatOne[1] != i:
          return "IMPOSSIBLE"
        meetColHavingOneStar = True
      else:
        return "IMPOSSIBLE"
    elif trueCount != 2:
      return "IMPOSSIBLE"
  if not meetColHavingOneStar:
    return "IMPOSSIBLE"
  return "POSSIBLE"
  pass


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    n = input()
    arr = []
    for _ in xrange(n):
      a = raw_input()
      aa = []
      for aaaa in a:
        if aaaa == '.':
          aa.append(False)
        else:
          aa.append(True)
      arr.append(aa)
    print "Case #" + str(t) + ": " + solve(arr)
