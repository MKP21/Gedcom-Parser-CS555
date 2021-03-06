from datetime import datetime
from datetime import timedelta
from time import strftime

import prettytable

from subscripts.outputDisplay import calculateage
from subscripts.userStories.UserStories_MP import getIndiByID, getFamByID


# Marriage before divorce
def us04(indi, fam, f):
    flag = True
    print("User Story 4 - Marriage before divorce, Running")
    for family in fam:
        # Gets divorce date of family
        div = family['DIV']

        # If family has no divorce date then continue
        if div == 'NA':
            continue
        # If div date exists then
        else:
            marr = family['MARR']
            if marr == 'NA':
                print(
                    f"No marraiage date found in family with id {family['FAM']}")

            if div < marr:
                print(
                    f"FAMILY: us04: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} ")
                f.write(
                    f"ERROR: FAMILY: us04: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} \n")
                flag = False

    # end of for loop
    if flag:
        print("User Story 4 Completed")
        return True
    else:
        print("User Story 4 Completed")
        return False


# Less than 150 years old

def us07(indi, fam, f):
    flag = True
    print("User Story 7 - Less than 150 years old, Running")
    for indv in indi:
        death = indv['DEAT']
        birth = indv['BIRT']
        # if Death date is defined for the individual
        if death != 'NA':
            no_of_days = (death - birth)
            if no_of_days > timedelta(days=54750):
                print(
                    f"INDIVIDUAL: us07: {indv['INDI']}: death {indv['DEAT']} after 150 years")
                f.write(
                    f"ERROR: INDIVIDUAL: us07: {indv['INDI']}: death {indv['DEAT']} after 150 years \n")
                flag = False
                # if Death date is not defined for the individual
        else:
            # current date
            cd = datetime.now()
            no_of_days = cd - birth
            if no_of_days > timedelta(days=54750):
                print(
                    f"person with name {indv['NAME']} and id {indv['INDI']} is more than 150 years from birth")
                f.write(
                    f"ERROR: INDIVIDUAL: us07: {indv['INDI']}: birth {indv['BIRT']} before 150 years from current date {cd} \n")
                flag = False
    # end of for loop
    if flag:
        print("User Story 7 Completed")
        return True
    else:
        print("User Story 7 Completed")
        return False


# Multiple births <= 5
def us14(indi, fam, f):
    flag = False
    print("User Story 14 - Multiple births <= 5, Running")
    for families in fam:
        # If number of children in a family is NA or <= 5 then continue
        if families['CHIL'] == 'NA' or len(families['CHIL']) <= 5:
            continue
        else:
            # if number of children in a family is more than 5

            # List to store birthdates of all children
            birthdates = []
            count = 1
            for child in families['CHIL']:
                for indv in indi:
                    if child == indv['INDI']:
                        birthdates.append(str(indv['BIRT']))

            for sib in range(len(birthdates) - 1):
                if birthdates[sib] == birthdates[sib + 1]:
                    count += 1
            if count > 5:
                print(
                    f"ERROR: FAMILY: US14: {families['FAM']}: has more than 5 siblings: {families['CHIL']}: who were born on the same date and time {birthdates}")
                f.write(
                    f"ERROR: FAMILY: US14: {families['FAM']}: has more than 5 siblings: {families['CHIL']}: who were born on the same date and time {birthdates}\n")
                flag = False
    # End of for loop

    if flag:
        print("User Story 14 Completed")
        return True
    else:
        print("User Story 14 Completed")
        return False


# Parents should not marry any of their children
def us17(indi, fam, f):
    print("Userstory 17 Running")
    parents = dict()
    for family in fam:
        if family['CHIL'] != 'NA':
            for children in family['CHIL']:
                parents[children] = (family['HUSB'], family['WIFE'])

    for family in fam:
        # if husband is parent of his wife
        if parents.__contains__(family['WIFE']) == True and family['HUSB'] in parents[family["WIFE"]]:
            print(
                f"ERROR: FAMILY: US17: {family['FAM']}: Husband {family['HUSB']} is married to the child {family['WIFE']}")
            f.write(
                f"ERROR: FAMILY: US17: {family['FAM']}: Husband {family['HUSB']} is married to the child {family['WIFE']}\n")
            print("Userstory 17 Completed")
            return False
        # if wife is parent of her husband
        elif parents.__contains__(family['HUSB']) == True and family['WIFE'] in parents[family['HUSB']]:
            print(
                f"ERROR: FAMILY: US17: {family['FAM']}: Wife {family['WIFE']} is married to the child {family['HUSB']}")
            f.write(
                f"ERROR: FAMILY: US17: {family['FAM']}: Wife {family['WIFE']} is married to the child {family['HUSB']}\n")
            print("Userstory 17 Completed")
            return False
    return True


# Unique families by spouses
def us24(indi, fam, f):
    print("Userstory 24 Running")
    famlist = list()
    flag = True
    for family in fam:
        current_fam_id = family['FAM']
        husband = getIndiByID(indi, family['HUSB'])['NAME']
        wife = getIndiByID(indi, family['WIFE'])['NAME']
        currList = [husband, wife, family['MARR']]
        if famlist.__contains__(currList):
            print(
                f"ERROR: FAMILY: US24: LINENUMBER: {family['FAM']}: has same named spouses {husband}, {wife} and marriage date {family['MARR']} with more than one family")
            f.write(
                f"ERROR: FAMILY: US24: LINENUMBER: {family['FAM']}: has same named spouses {husband}, {wife} and marriage date {family['MARR']} with more than one family \n")
            flag = False
        elif not famlist.__contains__(currList):
            famlist.append(currList)
    print("User Story 24 Completed")
    if flag:
        return True
    else:
        return False




# Include individual ages
def us27(indi, fam, f):
    print("Userstory 27 Running")
    list_of_age = list()
    flag = True
    for person in indi:
        if person['BIRT'] == 'NA':

            print(f"ERROR: INDIVIDUAL US27: no birth date found for {person['INDI']}")
            f.write(f"ERROR: INDIVIDUAL US27: no birth date found for {person['INDI']} \n")
            flag = False
        else:
            b_date = person['BIRT']
            d_date = person['DEAT']

            person_age = calculateage(b_date, d_date)
            list_of_age.append([person['INDI'], person['NAME'], person_age])
            ftable = prettytable.PrettyTable()
            ftable.field_names = ["INDI ID", "NAME", "AGE"]
    for l in list_of_age:
        ftable.add_row([l[0],l[1],l[2]])
    f.write(f"ERROR: INDIVIDUAL US27: list of individual's age : \n")
    f.write(f"{str(ftable)} \n")
    print("Userstory 27 Completed")
    if flag:
        return True
    else:
        return False


# List large age differences
def us34(indi, fam, f):
    print("Userstory 34 Running")
    flag = True
    for family in fam:
        # getting birthdates of both spouses
        husb_bdate = getIndiByID(indi, family['HUSB'])['BIRT']
        wife_bdate = getIndiByID(indi, family['WIFE'])['BIRT']

        days_in_year = 365.2425
        husb_age_at_marr = abs(int((family['MARR'] - husb_bdate).days / days_in_year))
        wife_age_at_marr = abs(int((family['MARR'] - wife_bdate).days / days_in_year))

        if husb_age_at_marr > wife_age_at_marr * 2:
            flag = False
            print(
                f"ERROR: FAMILY: US34: family with id {family['FAM']} had husband {family['HUSB']} of age {husb_age_at_marr} twice the age of his wife {family['WIFE']} of age {wife_age_at_marr} during their marriage {family['MARR']}")
            f.write(f"ERROR: FAMILY: US34: family with id {family['FAM']} had husband {family['HUSB']} of age {husb_age_at_marr} twice the age of his wife {family['WIFE']} of age {wife_age_at_marr} during their marriage {family['MARR']}\n")
        elif wife_age_at_marr > husb_age_at_marr * 2:
            flag = False
            print(
                f"ERROR: FAMILY: US34: family with id {family['FAM']} had wife {family['WIFE']} of age {wife_age_at_marr} twice the age of her husband {family['HUSB']} of age {husb_age_at_marr} during their marriage {family['MARR']}")
            f.write(f"ERROR: FAMILY: US34: family with id {family['FAM']} had wife {family['WIFE']} of age {wife_age_at_marr} twice the age of her husband {family['HUSB']} of age {husb_age_at_marr} during their marriage {family['MARR']}\n")
    print("Userstory 34 Completed")
    if flag:
        return True
    else:
        return False


# List recent survivors
def us37(indi, fam, f):
    print("Userstory 37 Running ")
    # f.write("List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days")
    # List of people who died in past 30 days
    dead_people_recent = list()
    # List of all the people who died
    dead_people_list = list()
    list_to_rtrn = list()
    for person in indi:
        if person['DEAT'] != 'NA':
            dead_people_list.append(person['INDI'])
            if abs(person['DEAT'] - datetime.today()) <= timedelta(days=30):
                dead_people_recent.append(person['INDI'])

    for dead_person in dead_people_recent:

        dead_person_obj = getIndiByID(indi, dead_person)

        if dead_person_obj['FAMS'] != 'NA':
            for family in dead_person_obj['FAMS']:
                family_obj = getFamByID(fam, family)

                if family_obj['HUSB'] == dead_person:
                    if not dead_people_list.__contains__(family_obj['WIFE']):
                        list_to_rtrn.append(family_obj['WIFE'])
                elif family_obj['WIFE'] == dead_person:
                    if not dead_people_list.__contains__(family_obj['HUSB']):
                        list_to_rtrn.append(family_obj['HUSB'])

                if family_obj['CHIL'] != 'NA':
                    children_list = family_obj['CHIL']

                    for child in range(len(children_list)):
                        if not dead_people_list.__contains__(children_list[child]):
                            list_to_rtrn.append(children_list[child])

    ftable = prettytable.PrettyTable()
    ftable.field_names = ["INDI ID", "NAME"]
    for i in range(len(list_to_rtrn)):
        person = getIndiByID(indi, list_to_rtrn[i])
        ftable.add_row([list_to_rtrn[i],person['NAME']])
    f.write(f"ERROR: INDIVIDUAL US37: List all living spouses and descendants of people who died in the last 30 days: \n")
    f.write(f"{str(ftable)} \n")
    print(f"{str(ftable)} \n")
    print("Userstory 37 Completed")
    return list_to_rtrn




