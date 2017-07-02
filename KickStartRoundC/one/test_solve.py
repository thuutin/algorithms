from unittest import TestCase
from easy import solve


class TestSolve(TestCase):
  def test_solve(self):
    self.assertEqual(solve("OMDU"), "SOUP")
    self.assertEqual(solve("BCB"), "AMBIGUOUS")
    self.assertEqual(solve("AOAAAN"), "BANANA")
    self.assertEqual(solve("YO"), "BANANA")
