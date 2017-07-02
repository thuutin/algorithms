from unittest import TestCase

from super_2048 import solve


def toInt(m):
  return map(int, m.split(" "))


class TestSolve(TestCase):
  def test(self):
    # self.assertEqual(solve(
    #   4, ["2 0 2 4",
    #       "2 0 4 2",
    #       "2 2 4 8",
    #       "2 2 4 4"], "right"
    # ), [[0, 0, 4, 4],
    #     [0, 2, 4, 2],
    #     [0, 4, 4, 8],
    #     [0, 0, 4, 8]])
    #
    # self.assertEqual(solve(
    #   3, ["2 2 2",
    #       "4 4 4",
    #       "8 8 8"
    #       ], "right"
    # ), [[0, 2, 4],
    #     [0, 4, 8],
    #     [0, 8, 16]])
    #
    # self.assertEqual(solve(
    #   3, ["2 2 2",
    #       "4 4 4",
    #       "8 8 8"
    #       ], "left"
    # ), [toInt("4 2 0"),
    #     toInt("8 4 0"),
    #     toInt("16 8 0")]
    # )

    # 4['0 0 2 4', '0 0 4 8', '0 2 16 32', '0 0 4 16']up

    self.assertEqual(solve(
      4, ['0 0 2 4',
          '0 0 4 8',
          '0 2 16 32',
          '0 0 4 16'], "up"
    ), [toInt("0 2 2 4"),
        toInt("0 0 4 8"),
        toInt("0 0 16 32"),
        toInt("0 0 4 16")]
    )

  pass
