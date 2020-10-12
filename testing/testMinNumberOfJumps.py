from AlgoExpert.minnumberofjumps import minNumberOfJumps
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfJumps(
            [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)
