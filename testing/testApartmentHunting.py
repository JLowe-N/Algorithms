from AlgoExpert import apartmenthunting as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        blocks = [
            {"gym": False, "school": True, "store": False},
            {"gym": True, "school": False, "store": False},
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": True, "store": True},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 3)
