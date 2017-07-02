from unittest import TestCase
from medium import solve


class TestSolve(TestCase):
  def testMe(self):
    self.assertEqual(solve(
      [
        [False, False, True],
        [True, True, False],
        [True, True, False],
      ]
    ), "POSSIBLE")

    self.assertEqual(solve(
      [
        [False, False, False],
        [True, True, True],
        [True, True, False],
      ]
    ), "IMPOSSIBLE")

  pass
