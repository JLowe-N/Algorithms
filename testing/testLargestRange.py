from AlgoExpert.largestrange import largestRange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRange(
            [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])
