from datetime import datetime

from subscripts.parseFile import fileParser
from subscripts.userStories.UserStories_Pratik_Deo import us01, us10, us15, us16, us21, us22
from subscripts.userStories.UserStories_MP import us03, us08, us13, us18, us23, us28
from subscripts.userStories.UserStories_MD import us04, us07, us14, us17
from subscripts.userStories.UserStories_DK import us02, us09, us12, us19, us30, us32
from subscripts.userStories.UserStories_AS import us05, us06, us11, us20

import unittest


class TestCases(unittest.TestCase):
    gedcom_error = "../sprint_03_v1.ged"
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

    def test_us11(self):
        f = open("test.txt", "a")
        value = us11(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us12(self):
        f = open("test.txt", "a")
        value = us12(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us13(self):
        f = open("test.txt", "a")
        value = us13(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us14(self):
        f = open("test.txt", "a")
        value = us14(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us15(self):
        f = open("test.txt", "a")
        value = us15(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us16(self):
        f = open("test.txt", "a")
        value = us16(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us17(self):
        f = open("test.txt", "a")
        value = us17(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us18(self):
        f = open("test.txt", "a")
        value = us18(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us19(self):
        f = open("test.txt", "a")
        value = us19(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us20(self):
        f = open("test.txt", "a")
        value = us20(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us21(self):
        f = open("test.txt", "a")
        value = us21(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us22(self):
        f = open("test.txt", "a")
        value = us22(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us23(self):
        f = open("test.txt", "a")
        value = us23(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us28(self):
        # test will fail if output list is not sorted by age
        f = open("test.txt", "a")
        value = us28(self.d[0], self.d[1], f)
        f.close()
        # us returns a list
        # will have to check if the list satisfies user story
        flag = True
        for family in value:
            lowest_date = datetime.min
            for child, birth in family:
                if lowest_date > birth:
                    flag = False
                    break
                lowest_date = birth
            if flag is False:
                break
        self.assertTrue(flag)

    def test_us30(self):
        f = open("test.txt", "a")
        value = us30(self.d[0], self.d[1], f)
        f.close()
        # Check if living married are greater than total number of individuals
        flag = True
        if len(value) > len(self.d[0]):
            flag = False
        self.assertTrue(flag)

    def test_us32(self):
        f = open("test.txt", "a")
        value = us32(self.d[2], f)
        f.close()
        self.assertFalse(value)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
