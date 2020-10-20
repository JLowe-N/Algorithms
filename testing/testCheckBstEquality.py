from AlgoExpert.checkbstequality import checkBstEquality
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.assertEqual(checkBstEquality(arrayOne, arrayTwo), True)
