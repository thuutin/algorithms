import math


def midOfThese(x, y):
  distance = math.sqrt((y[1] - x[1]) ** 2 + (y[0] - x[0]) ** 2)
  newDistance = distance * (y[2] / (y[2] + x[2]))
  # x[1] = a * x[0] + b
  # y[1] = a * y[0] + b
  if y[0] == x[0]:
    # x = x[0]
    root1X = x[0]
    root1Y = x[0] + newDistance
    root2X = x[0]
    root2Y = x[0] - newDistance
  else:
    a = (y[1] - x[1]) / (y[0] - x[0])
    b = x[1] - a * x[0]
    # ( Z[0] - x[0] ) ** 2 + ( Z[1] - x[1] ) ** 2 = newDistance ** 2
    # Z[1] = a * Z[0] + b

    # Z0  = math.sqrt(newDistance ** 2 -  ( a * Z[0] + b - x[1] ) ** 2) - x[0]
    A = a ** 2 + 1
    B = 2 * b * a - 2 * a * x[1] - 2 * x[0]
    C = x[0] ** 2 - 2 * b * x[1] + x[1] ** 2 - newDistance ** 2 + b ** 2

    root1X = (-1 * B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
    root1Y = a * root1X + b
    root2X = (-1 * B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
    root2Y = a * root2X + b
  if (root1X - x[0]) * (y[0] - x[0]) >= 0 and (root1Y - x[1]) * (y[1] - x[1]) >= 0:
    return root1X, root1Y, (x[2] + y[2])
  else:
    return root2X, root2Y, (x[2] + y[2])


T = input()
for t in xrange(1, T + 1):
  n = input()
  arr = []
  for _ in xrange(n):
    arr.append(map(float, raw_input().split(" ")))

  point = midOfThese(arr[0], arr[1])
  for i in xrange(2, len(arr)):
    point = midOfThese(point, arr[i])

  count = 0
  for i in xrange(n):
    count += max(abs(arr[i][0] - point[0]), abs(arr[i][1] - point[1]))

  print "Case #" + str(t) + ": " + "{0:.6f}".format(count)
