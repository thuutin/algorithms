from unittest import TestCase
from medium import solveIt

class TestSolveIt(TestCase):
  def testSolve(self):
    self.assertEqual(solveIt(7), 2)
    self.assertEqual(solveIt(13), 3)
    self.assertEqual(solveIt(21), 4)
    self.assertEqual(solveIt(97656), 5)
  pass
