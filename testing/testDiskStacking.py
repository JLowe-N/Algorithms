from AlgoExpert.diskstacking import diskStacking
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8],
                          [2, 3, 4], [2, 2, 1], [4, 4, 5]]),
            [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
        )
