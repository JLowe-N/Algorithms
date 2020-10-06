from AlgoExpert.shortenpath import shortenPath
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = "/foo/bar/baz"
        output = shortenPath("/foo/../test/../test/../foo//bar/./baz")
        self.assertEqual(output, expected)
