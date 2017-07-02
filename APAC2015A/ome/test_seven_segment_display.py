from unittest import TestCase
from seven_segment_display import seven_segment_display


class TestSeven_segment_display(TestCase):
  def test_seven_segment_display(self):
    self.assertEqual(seven_segment_display(
      "0010011 1011001".split(" ")), "ERROR!"
    )
    self.assertEqual(seven_segment_display(
      "0000000 0000000 0000000 0000000 0000000 0000000".split(" ")), "0000000"
    )

    self.assertEqual(seven_segment_display(
      ["0100000",
       "0000111",
       "0000011"]), "0100011"
    )

    self.assertEqual(seven_segment_display(
      ["1111111"]), "1110000"
    )
    self.assertEqual(seven_segment_display(
      ["1011011", "1011111", "1010000", "1011111", "1011011"]), "0010011"
    )

    self.assertEqual(seven_segment_display(
      ["1101011", "1100000"]), "1001011"
    )
    self.assertEqual(seven_segment_display(
      ["0000000", "0001010"]), "ERROR!"
    )

    self.assertEqual(seven_segment_display(
      "1011001 0110001".split(" ")), "1111001"
    )
