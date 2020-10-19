from AlgoExpert import mergesort as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.mergeSort([8, 5, 2, 9, 5, 6, 3]), [
                         2, 3, 5, 5, 6, 8, 9])
