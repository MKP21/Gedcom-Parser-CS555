from subscripts.parseFile import fileParser
from subscripts.userStories.UserStories_Pratik_Deo import us01, us10
from subscripts.userStories.UserStories_MP import us03, us08
from subscripts.userStories.UserStories_MD import us04, us07
from subscripts.userStories.UserStories_DK import us02, us09, us12, us19
from subscripts.userStories.UserStories_AS import us05, us06

import unittest


class TestCases(unittest.TestCase):
    gedcom_error = "../sprint_02_updated.ged"
    d = fileParser(gedcom_error)

    def test_us01(self):
        f = open("test.txt", "w+")
        value = us01(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us02(self):
        f = open("test.txt", "a")
        value = us02(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us03(self):
        f = open("test.txt", "a")
        value = us03(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us04(self):
        f = open("test.txt", "a")
        value = us04(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us05(self):
        f = open("test.txt", "a")
        value = us05(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us06(self):
        f = open("test.txt", "a")
        value = us06(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us07(self):
        f = open("test.txt", "a")
        value = us07(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us08(self):
        f = open("test.txt", "a")
        value = us08(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us09(self):
        f = open("test.txt", "a")
        value = us09(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us10(self):
        f = open("test.txt", "a")
        value = us10(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us12(self):
        f = open("test.txt", "a")
        value = us12(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us19(self):
        f = open("test.txt", "a")
        value = us19(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)
