def countBlue(s):
  count = 0
  for i in xrange(len(s)):
    if s[i] == 'B':
      count += 1
  return count


def solveIt(pat, x, y):
  left = (len(pat) - x % len(pat)) % len(pat)
  count = y - x + 1 - left
  mod = count % len(pat)
  return count / len(pat) * countBlue(pat) + countBlue(pat[:mod]) + countBlue(pat[len(pat) - left:])


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    pat = raw_input()
    x, y = map(int, raw_input().split(" "))
    r = solveIt(pat, x - 1, y - 1)
    print "Case #" + str(t) + ": " + str(r)
  pass
  # 3
  # BBRB
  # 4 8
  # BBRB
  # 10 12
  # BR
  # 1 1000000
