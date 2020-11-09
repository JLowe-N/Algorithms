from AlgoExpert import maxprofitwithktransactions as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2), 93)
