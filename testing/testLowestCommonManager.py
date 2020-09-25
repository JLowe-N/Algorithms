from AlgoExpert import lowestcommonmanager as program
import unittest


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)


ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getOrgCharts():
    orgCharts = {}
    for letter in ALPHABET:
        orgCharts[letter] = OrgChart(letter)
    return orgCharts


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        orgCharts = getOrgCharts()
        orgCharts["A"].addDirectReports([orgCharts["B"], orgCharts["C"]])
        orgCharts["B"].addDirectReports([orgCharts["D"], orgCharts["E"]])
        orgCharts["C"].addDirectReports([orgCharts["F"], orgCharts["G"]])
        orgCharts["D"].addDirectReports([orgCharts["H"], orgCharts["I"]])

        lcm = program.getLowestCommonManager(orgCharts["A"], orgCharts["E"], orgCharts["I"])
        self.assertEqual(lcm.name, "B")
