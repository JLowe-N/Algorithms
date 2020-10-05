from AlgoExpert.levenshteindistance import levenshteinDistance
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)
