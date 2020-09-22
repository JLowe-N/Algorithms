from AlgoExpert.subarraysort import subarraySort
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subarraySort(
            [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])
