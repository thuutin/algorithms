from unittest import TestCase


class Node:
  def __init__(self, val, next):
    self.val = val
    self.next = next


def isLinkedListAPalindrome(head):
  if head is None:
    return False
  list = []
  c = head
  detect = set()
  while c is not None:
    if c in detect:
      return False
    detect.add(c)
    list.append(c.val)
    c = c.next
  i = 0
  j = len(list) - 1
  while i < j:
    if list[i] != list[j]:
      return False
    i += 1
    j -= 1
  return True
