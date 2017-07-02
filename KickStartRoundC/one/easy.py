import sys


# sys.stdin = file("/Users/tin/Downloads/A-small-attempt0.in")
def c(n):
  return chr(n + 65)


def n(c):
  return ord(c) - 65

def solve(s):
  if len(s) % 2 == 1:
    return "AMBIGUOUS"

  if len(s) == 2:
    return s[1] + s[0]

  de = []
  for ss in s:
    de.append(n(ss))


  en = [None] * len(de)
  en[1] = de[0]
  i = 3
  while i < len(de):
    en[i] = (de[i - 1] - en[i - 2]) % 26
    i += 2

  en[-2] = de[len(de) - 1]
  i = len(de) - 4
  while i >=0 :
    en[i] = (de[i + 1] - en[i + 2]) % 26
    i -= 2

  ssss = ""
  for e in en:
    ssss += c(e)

  return ssss

if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    print "Case #" + str(t) + ": " + solve(raw_input())
