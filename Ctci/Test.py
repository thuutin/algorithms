from unittest import TestCase
from linkedlist_is_palindrome import isLinkedListAPalindrome
from linkedlist_is_palindrome import Node


class LinkedListAPalindromeTest(TestCase):
  def testSomeBaseCases(self):
    self.assertTrue(isLinkedListAPalindrome(
      Node("a", Node("b", Node("a", None)))
    ))

  def testSingleElem(self):
    self.assertTrue(isLinkedListAPalindrome(
      Node("a", None)
    ))

  def testEvenLength(self):
    self.assertTrue(isLinkedListAPalindrome(
      Node("a", Node("a", None))
    ))

  def testLength(self):
    self.assertFalse(isLinkedListAPalindrome(
      Node("a", Node("b", None))
    ))

  def testNone(self):
    self.assertFalse(isLinkedListAPalindrome(
      None
    ))
  def testCycleLinkedList(self):
    b = Node("b", Node("c", None))
    head = Node("a", b)
    b.next.next = b
    self.assertFalse(isLinkedListAPalindrome(
      head
    ))