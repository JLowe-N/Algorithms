from AlgoExpert import calendarmatching as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 30
        expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
        result = program.calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)
