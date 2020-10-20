from AlgoExpert.zigzagtraverse import zigzagTraverse
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
