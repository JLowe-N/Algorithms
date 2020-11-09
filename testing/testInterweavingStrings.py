from AlgoExpert import interweavingstrings as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(program.interweavingStrings(one, two, three), True)
