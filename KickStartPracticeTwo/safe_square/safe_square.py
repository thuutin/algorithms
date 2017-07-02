def solve(r, c, monsters):
  monsterHash = set()

  for i in monsters:
    monsterHash.add((i[0], i[1]))

  countArray = []
  for i in xrange(r):
    countArray.append([0] * c)
  ans = 0
  temp = [0] * 3
  for i in xrange(r):
    for j in xrange(c):
      if (i, j) in monsterHash:
        continue

      for _ in xrange(3):
        temp[_] = 0

      if i == 0 and j == 0:
        countArray[i][j] = 1
        ans += countArray[i][j]
        continue

      if j > 0:
        temp[0] = countArray[i][j - 1]

      if i > 0:
        temp[1] = countArray[i - 1][j]

      if i > 0 and j > 0:
        temp[2] = countArray[i - 1][j - 1]

      countArray[i][j] = min(temp) + 1
      ans += countArray[i][j]
  return ans


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    r, c, k = map(int, raw_input().split(" "))
    monsters = []
    for _ in xrange(k):
      m = map(int, raw_input().split(" "))
      monsters.append((m[0], m[1]))
    print "Case #" + str(t) + ":", solve(r, c, monsters)
