from AlgoExpert.binarysearch import binarySearch 
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_2(self):
        self.assertEqual(binarySearch([], 33), -1)

    def test_case_3(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], -10), 0)

    def test_case_4(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], -5), 1)
    
    def test_case_5(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 0), 2)

    def test_case_6(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 3), 4)

    def test_case_7(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 10), 5)

    def test_case_8(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 25), 6)

    
    def test_case_9(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 88), 7)
    
    def test_case_10(self):
        self.assertEqual(binarySearch([-10, -5, 0, 3, 3, 10, 25, 88, 4324], 4324), 8)
