from AlgoExpert.patternmatcher import patternMatcher
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(patternMatcher(
            "xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])
