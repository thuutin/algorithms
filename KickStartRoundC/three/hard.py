import sys

sys.stdin = file("/Users/tin/Downloads/C-large-practice.in")


def solve(Q, mine, him, score):
  him = him[0]
  score = score[0]
  same = 0
  for i in xrange(Q):
    if mine[i] == him[i]:
      same += 1

  diff = Q - same
  if score <= same:
    return score + diff
  else:
    return Q - (score - same)


def solve2(Q, mine, him, score):
  if len(him) == 1:
    return solve(Q, mine, him, score)

  A = B = C = D = 0
  for i in xrange(Q):
    if mine[i] == him[0][i] == him[1][i]:
      A += 1
    elif mine[i] == him[0][i]:
      B += 1
    elif mine[i] == him[1][i]:
      C += 1
    else:
      D += 1
  Arange = min(score[0], score[1], A)
  X = score[0] - C - D
  Y = score[1] - D - B
  # y - z = (X - Y) / 2
  ret = 0
  # for i in xrange(Arange + 1):
  #   x = i
  #   w = x - (X + Y) / 2
  #   for j in xrange(B + 1):
  #     y = j
  #     z = y - (X - Y) / 2
  #     if w >= 0 and z >= 0:
  #       ret = max(ret, x + y + z + w)

  for x in xrange(A + 1):
    for y in xrange(B + 1):
      for z in xrange(C + 1):
        for w in xrange(D + 1):
          if x + y + C - z + D - w == score[0] and x + B - y + z + D - w == score[1]:
            ret = max(ret, x + y + w + z)

  return ret


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    N, Q = map(int, raw_input().split(" "))
    him = []
    for n in xrange(N):
      him.append(raw_input())
    mine = raw_input()
    score = map(int, raw_input().split(" "))
    print "Case #" + str(t) + ": " + str(solve2(Q, mine, him, score))
