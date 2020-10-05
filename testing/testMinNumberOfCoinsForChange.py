from AlgoExpert.minnumofcoinsforchange import minNumberOfCoinsForChange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 5, 10]), 3)
