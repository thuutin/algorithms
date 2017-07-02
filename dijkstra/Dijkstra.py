import sys
from collections import deque
import heapq
from algorithms.sorting import bubble_sort

t = int(raw_input().strip())
for a0 in xrange(t):
  n, m = raw_input().strip().split(' ')
  n, m = [int(n), int(m)]
  graph = {}
  w = {}
  distance = [-1] * (n + 1)
  for a1 in xrange(m):
    x, y, r = raw_input().strip().split(' ')
    x, y, r = [int(x), int(y), int(r)]
    if (x, y) not in w or w[(x, y)] > r:
      w[(x, y)] = r

    if (y, x) not in w or w[(y, x)] > r:
      w[(y, x)] = r

    if x in graph:
      graph[x].add(y)
    else:
      graph[x] = {y}
    if y in graph:
      graph[y].add(x)
    else:
      graph[y] = {x}
  # print graph
  # print w
  s = int(raw_input().strip())
  distance[s] = 0

  heap = [(0, s)]

  visisted = set()
  while len(heap) > 0:
    now = heapq.heappop(heap)[1]
    if now in visisted:
      continue
    visisted.add(now)

    neighbor = graph[now]
    #print neighbor
    for node in neighbor:
      if distance[node] == -1 or distance[node] > distance[now] + w[(now, node)]:
        distance[node] = distance[now] + w[(now, node)]
      heapq.heappush(heap, (distance[node], node))
      # print neighbor
      # print now
      # print distance[1:]
  # print distance
  for i in xrange(1, len(distance)):
    if i == s:
      continue
    print distance[i],
  print
