from AlgoExpert.knapsackproblem import knapsackProblem
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knapsackProblem(
            [[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])
