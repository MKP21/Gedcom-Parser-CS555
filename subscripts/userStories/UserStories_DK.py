from datetime import datetime
from datetime import timedelta


# Birth before Marriage
def us02(indi, fam, f):
    print("User Story 2 - Birth before Marriage, Running")
    # SETTING 8
    flag = True
    for families in fam:
        for person in indi:
            if families['HUSB'] == person['INDI'] or families['WIFE'] == person['INDI']:
                # CHECK IF PERSON HAS BIRTHDATE
                if person['BIRT'] == 'NA':
                    print("NO BIRTHDATE FOUND")
                    f.write(
                        f"Error: INDIVIDUAL: US02: { person['INDI']} {person['NAME']} birthdate not found \n")
                    flag = False
                # SETTING M = BIRTHDATE
                m = person['BIRT']
                # COMPARING MARRIAGE DATE TO BIRTHDATE
                if families['MARR'] < m:
                    print(
                        f" User Story 02  Error: {person['INDI']} {person['NAME']} was born after marriage")
                    f.write(
                        f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} was born after marriage\n")
                    flag = False
    if flag:
        print("User Story 2 Completed")
        return True
    else:
        return False

# Birth before death of parents


def us09(indi, fam, f):
    print("User Story 9 - Birth before death of parents, Running")
    # SETTING FLAG
    flag = True
    for family in fam:
        fatherdeath = 'NA'
        motherdeath = 'NA'
        # CHECKING FOR DEATH DATES OF MOTHER AND FATHER
        for person in indi:
            if family["HUSB"] == person["INDI"]:
                if person["DEAT"] != 'NA':
                    fatherdeath = person["DEAT"] + timedelta(weeks=36)

            if family["WIFE"] == person["INDI"]:
                if person["DEAT"] != 'NA':
                    motherdeath = person["DEAT"]
        if family["CHIL"] != 'NA':
            for child in family["CHIL"]:
                childobj = next(
                    (item for item in indi if item["INDI"] == child), False)
                if childobj != "NA" and fatherdeath != "NA" and motherdeath != "NA":
                    # checking if child is born after death of parents
                    if childobj["BIRT"] > motherdeath or childobj["BIRT"] > fatherdeath:
                        print(
                            f"Indi id -> {childobj['INDI']}, Birth after death of parents")
                        f.write(
                            f"Error: INDIVIDUAL: US09: {childobj['INDI']} {childobj['NAME']} Birth after death of parents  \n")
                        flag = False
    if flag:
        print("User Story 9 Completed")
        return True
    else:
        return False
