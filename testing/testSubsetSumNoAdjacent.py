from AlgoExpert.maxsubsetsumnoadjacent import maxSubsetSumNoAdjacent
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)
