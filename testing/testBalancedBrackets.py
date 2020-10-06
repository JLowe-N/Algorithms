from AlgoExpert.balancedbrackets import balancedBrackets
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)
