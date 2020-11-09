from AlgoExpert import numberofbinarytreetopologies as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.numberOfBinaryTreeTopologies(3), 5)
