from datetime import datetime
from datetime import timedelta
from subscripts.userStories.UserStories_MP import getIndiByID, getFamByID
from subscripts.userStories.UserStories_Pratik_Deo import getAgeById


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
                        f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} birthdate not found \n")
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


# Parents should not be too old User Story 12

def us12(indi, fam, f):
    print("User Story 12 - Parents  not too old , Running")
    flag = True
    for family in fam:
        fatherbirth = 'NA'
        motherbirth = 'NA'
        # CHECKING FOR BIRTH DATES OF MOTHER AND FATHER
        for person in indi:
            if family["HUSB"] == person["INDI"]:
                if person["BIRT"] != 'NA':
                    fatherbirth = person["BIRT"] + timedelta(weeks=4171.43)
            if family["WIFE"] == person["INDI"]:
                if person["BIRT"] != 'NA':
                    motherbirth = person["BIRT"] + timedelta(weeks=3128.57)
        if family["CHIL"] != 'NA':
            for child in family["CHIL"]:
                childobj = next(
                    (item for item in indi if item["INDI"] == child), False)
                if childobj != "NA" and fatherbirth != "NA" and motherbirth != "NA":
                    # checking if child is born after death of parents
                    if childobj["BIRT"] > motherbirth or childobj["BIRT"] > fatherbirth:
                        print(
                            f"Indi id -> {childobj['INDI']}, Parents are too old")
                        f.write(
                            f"Error: INDIVIDUAL: US12: {childobj['INDI']} {childobj['NAME']} Parents are too old\n")
                        flag = False
    if flag:
        print("User Story 9 Completed")
        return True
    else:
        return False


def us19(indi, fam, f):
    flag = True
    print("User Story 19 - First cousins should not marry, running")
    for family in fam:
        grandfatherfamc = 0
        grandmotherfamc = 1
        husband = getIndiByID(indi, family["HUSB"])  # Getting Husband Data
        if husband["FAMC"] != 'NA':
            husbandfamc = getFamByID(fam, husband["FAMC"][0])
            # Getting Husband family child id
            if husbandfamc["HUSB"] != 'NA':
                grandfather = getIndiByID(indi, husbandfamc["HUSB"])
                # Comparing family id of paternal grandfather
                if grandfather["FAMC"] != 'NA':
                    grandfatherfamc = getFamByID(fam, grandfather["FAMC"][0])
                else:
                    # if match not found setting random value
                    grandfatherfamc = 0
            if husbandfamc["WIFE"] != 'NA':
                grandmother = getIndiByID(indi, husbandfamc["WIFE"])
                if grandmother["FAMC"] != 'NA':
                    grandmotherfamc = getFamByID(fam, grandmother["FAMC"][0])
                else:
                    # if match not found setting random value
                    grandmotherfamc = 1
        wife = getIndiByID(indi, family["WIFE"])
        if wife["FAMC"] != 'NA':
            wifefamc = getFamByID(fam, wife["FAMC"][0])
            # Comparing family id of maternal grandfather
            if wifefamc["HUSB"] != 'NA':
                wgrandfather = getIndiByID(indi, wifefamc["HUSB"])
                if wgrandfather["FAMC"] != 'NA':
                    wgrandfatherfamc = getFamByID(fam, wgrandfather["FAMC"][0])
                else:
                    # if match not found setting random value
                    wgrandfatherfamc = 2
            if wifefamc["WIFE"] != 'NA':
                wgrandmother = getIndiByID(indi, wifefamc["WIFE"])
                if wgrandmother["FAMC"] != 'NA':
                    wgrandmotherfamc = getFamByID(fam, wgrandmother["FAMC"][0])
                else:
                    # if match not found setting random value
                    wgrandmotherfamc = 3

            if wgrandfatherfamc == grandfatherfamc or wgrandfatherfamc == grandmotherfamc or wgrandmotherfamc == grandmotherfamc or wgrandmotherfamc == grandfatherfamc:
                print(f'Error: FAMILY: US19: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins')
                f.write(f'Error: FAMILY: US19: spouses {family["HUSB"]} and {family["WIFE"]} are first cousins')
                flag = False

    print("User Story 19 Completed")
    return flag


def us30(indi, fam, f):
    print("User Story 30 - List all living married, running")
    living_married = list()
    # Iterating over indi
    for individual in indi:
        # If Alive
        if individual["DEAT"] == "NA":
            # If has Wife
            if individual["FAMS"] != "NA":
                # Append to List
                living_married.append(individual)

    print("User Story 30 Completed")
    return living_married


def us32(us32p, f):
    # Listing multiple births in parser itself so just passing the list
    flag = True
    if len(us32p) != 0:
        for mulbirth in us32p:
            print(
                f"Indi id -> {mulbirth}, has multiple births")
            f.write(
                f"Error: INDIVIDUAL: US32: {mulbirth}, has multiple births\n")
            flag = False
    print("User Story 32 Completed")
    return flag


def us35(indi, fam, f):
    # Created empty list to store recent births
    recent_birth = list()
    print("User Story 35-List recent births")
    # Iterating over individuals
    for individuals in indi:
        # Getting todays date
        todays_date = datetime.today()
        age = individuals["BIRT"]
        # Comparing today's date to 30 days constraint
        if 0 < (todays_date - age).days <= 30:
            recent_birth.append(individuals)

    print("User Story 35 Completed")
    return recent_birth


def us39(indi, fam, f):
    print("User Story 39 - List upcoming Anniversary, running")
    # Created empty list to store upcoming anniversary
    upcoming_anniversary = list()
    # Iterating in families to check over each marriage
    for families in fam:
        # Getting Data of Husband and Wife to check if they are alive
        husband = getIndiByID(indi, families["HUSB"])
        wife = getIndiByID(indi, families["WIFE"])
        if wife["DEAT"] == "NA" and husband["DEAT"] == "NA":
            # Checking there marriage with current date
            todays_date = datetime.today()
            aniversary = families["MARR"]
            # To do math operation changing year to current date
            aniversary = aniversary.replace(year=todays_date.year)

            if 0 < (aniversary - todays_date).days <= 30:
                # If criteria matches we append object to list
                upcoming_anniversary.append(husband)
                upcoming_anniversary.append(wife)

    print("User Story 39 Completed")
    return upcoming_anniversary
