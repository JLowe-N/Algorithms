from AlgoExpert.minrewards import minRewards
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)
