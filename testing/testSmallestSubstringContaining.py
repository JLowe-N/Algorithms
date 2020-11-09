from AlgoExpert import smallestsubstringcontaining as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        bigString = "abcd$ef$axb$c$"
        smallString = "$$abf"
        expected = "f$axb$"
        self.assertEqual(program.smallestSubstringContaining(bigString, smallString), expected)
