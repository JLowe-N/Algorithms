from AlgoExpert.fournumbersum import fourNumberSum
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [7, 6, 4, -1, 1, 2]
        targetSum = 16
        quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertEqual(fourNumberSum(array, targetSum), quadruplets)
