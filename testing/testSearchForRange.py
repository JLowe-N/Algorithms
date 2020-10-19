from AlgoExpert.searchforrange import searchForRange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4, 9])
