from AlgoExpert import knuthmorrispratt as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.knuthMorrisPrattAlgorithm(
            "aefoaefcdaefcdaed", "aefcdaed"), True)
