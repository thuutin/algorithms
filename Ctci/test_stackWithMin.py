from unittest import TestCase
from stack_with_min import StackWithMin


class TestStackWithMin(TestCase):

  def testPushAndPop(self):
    stack = StackWithMin()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    self.assertEqual(stack.pop(), 4)
    self.assertEqual(stack.pop(), 3)
    self.assertEqual(stack.pop(), 2)
    self.assertEqual(stack.pop(), 1)

  def testPushAndPop2(self):
    stack = StackWithMin()
    stack.push(10)
    stack.push(5)
    self.assertEqual(stack.pop(), 5)
    stack.push(9)
    stack.push(3)
    self.assertEqual(stack.pop(), 3)

  def testMin(self):
    stack = StackWithMin()
    stack.push(10)
    stack.push(5)
    self.assertEqual(stack.getMin(), 5)
    stack.push(3)
    stack.push(9)
    self.assertEqual(stack.getMin(), 3)