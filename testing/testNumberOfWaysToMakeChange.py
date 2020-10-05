from AlgoExpert.numberofwaystomakechange import numberOfWaysToMakeChange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)
