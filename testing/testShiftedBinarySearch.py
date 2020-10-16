from AlgoExpert.shiftedbinarysearch import shiftedBinarySearch
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33), 8)
