from unittest import TestCase
from hard import Range
from hard import solveIt


class TestRange(TestCase):
  def test_intersect(self):
    self.assertEqual(Range(1, 3).intersect(Range(2, 3)), 2)
    self.assertEqual(Range(3, 10).intersect(Range(3, 10)), 8)
    self.assertEqual(Range(7, 10).intersect(Range(1, 7)), 1)
    self.assertEqual(Range(7, 10).intersect(Range(8, 10)), 3)
    self.assertEqual(Range(7, 10).intersect(Range(7, 10)), 4)
    self.assertEqual(Range(7, 10).intersect(Range(8, 1000)), 3)
    self.assertEqual(Range(7, 100).intersect(Range(50, 60)), 11)


class TestSolve(TestCase):
  def testInterval(self):
    self.assertEqual(
      solveIt(
        [(2, 5),  (4, 7), (3, 5)]), 4
    )
