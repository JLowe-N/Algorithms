from AlgoExpert.multistringsearch import multiStringSearch
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            multiStringSearch("this is a big string", [
                              "this", "yo", "is", "a", "bigger", "string", "kappa"]),
            [True, False, True, True, False, True, False],
        )
