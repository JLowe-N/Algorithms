from AlgoExpert.quickselect import quickselect
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickselect([8, 5, 2, 9, 7, 6, 3], 3), 5)
