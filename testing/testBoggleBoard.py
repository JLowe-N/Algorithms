from AlgoExpert import boggleboard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["t", "h", "i", "s", "i", "s", "a"],
            ["s", "i", "m", "p", "l", "e", "x"],
            ["b", "x", "x", "x", "x", "e", "b"],
            ["x", "o", "g", "g", "l", "x", "o"],
            ["x", "x", "x", "D", "T", "r", "a"],
            ["R", "E", "P", "E", "A", "d", "x"],
            ["x", "x", "x", "x", "x", "x", "x"],
            ["N", "O", "T", "R", "E", "-", "P"],
            ["x", "x", "D", "E", "T", "A", "E"],
        ]
        words = ["this", "is", "not", "a", "simple", "boggle",
                 "board", "test", "REPEATED", "NOTRE-PEATED"]
        expected = ["this", "is", "a", "simple",
                    "boggle", "board", "NOTRE-PEATED"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)
