from AlgoExpert import rightsmallerthan as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [8, 5, 11, -1, 3, 4, 2]
        expected = [5, 4, 4, 0, 1, 1, 0]
        actual = program.rightSmallerThan(array)
        self.assertEqual(expected, actual)
