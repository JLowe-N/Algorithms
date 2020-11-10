from AlgoExpert import longestincreasingsubsequence as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]), [-24, 2, 3, 5, 6, 35]
        )
