from subscripts.parseFile import fileParser
from subscripts.userStories.UserStories_AS import us05

import unittest


class TestCases(unittest.TestCase):
    gedcom_error = "../My-Family-27-Jan-2020-330.ged"
    d = fileParser(gedcom_error)

    def test_us05(self):
        f = open("test.txt", "w+")
        value = us05(self.d[0], self.d[1], f)
        f.close()
        self.assertTrue(value)
