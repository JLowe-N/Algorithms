from AlgoExpert.kadanesalgorithm import kadanesAlgorithm
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kadanesAlgorithm(
            [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)
