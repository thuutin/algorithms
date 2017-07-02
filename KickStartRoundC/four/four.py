def solve(big, small, median, mean):
  if small > big or median > big or mean > big or mean < small or median < small:
    return "IMPOSSIBLE"
  if big == small:
    return 1

  if mean == median == (big + small) / 2:
    return 2

  dep = 3
