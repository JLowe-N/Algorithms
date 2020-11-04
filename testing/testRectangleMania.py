from AlgoExpert import rectanglemania as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0],
                  [2, 1], [2, 0], [3, 1], [3, 0]]
        self.assertEqual(program.rectangleMania(coords), 6)
