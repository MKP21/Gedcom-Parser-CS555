from subscripts.parseFile import fileParser
from subscripts.userStories.UserStories_AS import us05

import unittest

class TestCases(unittest.TestCase):

    gedcom_error = open("My-Family-27-Jan-2020-330","r")
    d = fileParser(gedcom_error)
    f = open("testing","w")

    def test_us05(self):
        self.assertTrue(us05(d[0],d[1],f))
        