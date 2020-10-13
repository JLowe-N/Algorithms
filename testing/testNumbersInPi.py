from AlgoExpert.numbersinpi import numbersInPi
import unittest


PI = "3141592653589793238462643383279"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numbers = ["314159265358979323846", "26433", "8",
                   "3279", "314159265", "35897932384626433832", "79"]
        self.assertEqual(numbersInPi(PI, numbers), 2)
