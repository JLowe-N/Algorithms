from AlgoExpert.maxsumincreasingsubsequence import maxSumIncreasingSubsequence
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]), [110, [10, 20, 30, 50]])
