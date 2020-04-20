from datetime import datetime

from subscripts.outputDisplay import calculateage
from subscripts.parseFile import fileParser
from subscripts.userStories.UserStories_Pratik_Deo import us01, us10, us15, us16, us21, us22, us29, us31
from subscripts.userStories.UserStories_MP import us03, us08, us13, us18, us23, us28, us38, us33, getIndiByID, \
    getFamByID
from subscripts.userStories.UserStories_MD import us04, us07, us14, us17, us24, us27, us34, us37
from subscripts.userStories.UserStories_DK import us02, us09, us12, us19, us30, us32, us39, us35
from subscripts.userStories.UserStories_AS import us05, us06, us11, us20, us25, us26, us36, us42

import unittest


class TestCases(unittest.TestCase):
    gedcom_error = "../sprint_04_v1.ged"
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

    def test_us24(self):
        f = open("test.txt", "a")
        value = us24(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us25(self):
        f = open("test.txt", "a")
        value = us25(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us26(self):
        f = open("test.txt", "a")
        value = us26(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us27(self):
        f = open("test.txt", "a")
        value = us27(self.d[0], self.d[1], f)
        f.close()
        self.assertTrue(value)

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

    def test_us29(self):
        f = open("test.txt", "a")
        value = us29(self.d[0], self.d[1], f)
        flag = False
        for id in value:
            person = getIndiByID(self.d[0], id)
            if person['DEAT'] != 'NA':
                flag = True
        f.close()
        self.assertTrue(flag)

    def test_us31(self):
        f = open("test.txt", "a")
        value = us31(self.d[0], self.d[1], f)
        flag = False
        for id in value:
            person = getIndiByID(self.d[0], id)
            age = calculateage(person["BIRT"], person["DEAT"])
            if (person["DEAT"] == 'NA' and person["FAMS"] == 'NA'):
                if (str(age) > '30'):
                    flag = True
        f.close()
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

    def test_us33(self):
        # list of orphaned kids
        f = open("test.txt", "a")
        value = us33(self.d[0], self.d[1], f)
        f.close()
        flag = True
        if len(value) == 0:
            flag = False
        for individual in value:
            if individual["DEAT"] != "NA" or int(calculateage(individual["BIRT"], "NA")) > 18:
                flag = False
                break
            indi_famc = getFamByID(self.d[1], individual["FAMC"][0])
            indi_mom = getIndiByID(self.d[0], indi_famc["WIFE"])
            indi_dad = getIndiByID(self.d[0], indi_famc["HUSB"])
            if indi_dad["DEAT"] == "NA" or indi_mom["DEAT"] == "NA":
                flag = False
                break

        self.assertTrue(flag)

    def test_us34(self):
        f = open("test.txt", "a")
        value = us34(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us35(self):
        f = open("test.txt", "a")
        value = us35(self.d[0], self.d[1], f)
        f.close()
        self.assertTrue(value)

    def test_us36(self):
        f = open("test.txt", "a")
        value = us36(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us37(self):
        f = open("test.txt", "a")
        value = us37(self.d[0], self.d[1], f)
        flag = True
        for id in value:
            person = getIndiByID(self.d[0], id)
            if person['DEAT'] != 'NA':
                flag = False
        f.close()
        self.assertTrue(flag)

    def test_us38(self):
        # test will fail if a persons birthday in the list is not in the next 30 days
        f = open("test.txt", "a")
        value = us38(self.d[0], self.d[1], f)
        f.close()
        flag = True
        for individual in value:
            curr_date = datetime.today()
            birth_day = individual["BIRT"]
            birth_day = birth_day.replace(year=curr_date.year)
            if birth_day < curr_date:
                birth_day = birth_day.replace(year=curr_date.year + 1)
            if (birth_day - curr_date).days > 30:
                flag = False
        self.assertTrue(flag)

    def test_us39(self):
        f = open("test.txt", "a")
        value = us39(self.d[0], self.d[1], f)
        f.close()
        self.assertTrue(value)

    def test_us42(self):
        f = open("test.txt", "a")
        value = us42(self.d[2], f)
        f.close()
        self.assertFalse(value)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
