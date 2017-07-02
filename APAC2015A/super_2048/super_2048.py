from collections import deque
import types


def toNum(matrix):
  matrixM = []
  for m in matrix:
    matrixM.append(map(int, m.split(" ")))
  return matrixM


def solve(n, matrix, direction):
  if type(matrix[0]) is types.StringType:
    matrix = toNum(matrix)

  if direction == "right":
    for m in xrange(n):
      now = matrix[m]
      firstNonzero = None
      for i in xrange(n - 1, -1, -1):
        if now[i] != 0:
          firstNonzero = i
          break

      if firstNonzero is None:
        matrix[m] = [0] * n
        continue

      stack = deque([now[firstNonzero]])
      i = firstNonzero - 1
      justDone = False
      while i >= 0:
        if now[i] == 0:
          i -= 1
          continue
        if stack[0] == now[i] and not justDone:
          stack[0] *= 2
          justDone = True
        else:
          stack.appendleft(now[i])
          justDone = False
        i -= 1
      replace = [0] * n
      for i in xrange(len(stack)):
        replace[i + n - len(stack)] = stack[i]
      matrix[m] = replace
  else:
    if direction == "left":
      new = []
      for m in xrange(n):
        matrix[m].reverse()
        new.append(matrix[m])
      needToRotate = solve(n, new, "right")
      newnew = []
      for n in needToRotate:
        n.reverse()
        newnew.append(n)
      return newnew
    elif direction == "up":
      newM = []
      for i in xrange(n):
        col = []
        for j in xrange(n - 1, -1, -1):
          col.append(matrix[j][i])
        newM.append(col)
      needToRotate = solve(n, newM, "right")
      newnew = []
      for i in xrange(n - 1, -1, -1):
        col = []
        for j in xrange(n):
          col.append(needToRotate[j][i])
        newnew.append(col)
      return newnew
      pass
    elif direction == "down":
      newM = []
      for i in xrange(n - 1, -1, -1):
        col = []
        for j in xrange(n):
          col.append(matrix[j][i])
        newM.append(col)
      needToRotate = solve(n, newM, "right")
      newnew = []
      for i in xrange(n):
        col = []
        for j in xrange(n - 1, -1, -1):
          col.append(needToRotate[j][i])
        newnew.append(col)
      return newnew
      pass

  return matrix


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    n, direction = raw_input().split()
    n = int(n)
    arr = []
    for _ in xrange(n):
      arr.append(raw_input())
    # print n, direction
    # for a in arr:
    #   print a

    mat = solve(n, arr, direction)
    print "Case #" + str(t) + ":"
    for m in mat:
      print " ".join(map(str, m))
