from AlgoExpert.longestsubstringwithoutduplication import longestSubstringWithoutDuplication
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestSubstringWithoutDuplication(
            "clementisacap"), "mentisac")
