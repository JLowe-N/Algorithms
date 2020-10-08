from AlgoExpert.longestcommonsubsequence import longestCommonSubsequence
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
        self.assertEqual(output, ["X", "Y", "Z", "W"])
