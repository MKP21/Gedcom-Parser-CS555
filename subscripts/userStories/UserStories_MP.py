from datetime import datetime
from datetime import timedelta

# Birth before death
from subscripts.outputDisplay import calculateage


def us03(indi, fam, f):
    flag = True
    print("User Story 03 - Birth before death, Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"Error: INDIVIDUAL: US03: {person['INDI']} {person['NAME']} were born before they died")
            f.write(f"Error: INDIVIDUAL: US03: {person['INDI']} {person['NAME']} were born before they died \n")
            flag = False

    print("User Story 03 Completed")
    return flag


# Birth before marriage of parent
def us08(indi, fam, f):
    flag = True
    print("User Story 08 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        if family["CHIL"] is "NA":
            continue
        for child in family["CHIL"]:
            childobj = next((item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                if family["DIV"] != "NA" and childobj["BIRT"] > family["DIV"] + timedelta(days=273.93188):
                    print(
                        f" Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of parents")
                    f.write(
                        f"Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of "f"parents \n")
                    flag = False
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth before marriage of parents")
                f.write(f"Error: INDIVIDUAL: US08: -> {childobj['INDI']}, Birth before marriage of parents \n")
                flag = False
            else:
                print(f'Error: INDIVIDUAL: US08: child with id {child} does not exist in indi list')
                f.write(f"Error: INDIVIDUAL: US08:child with id {child} does not exist in indi list \n")
                flag = False

    print("User Story 08 Completed")
    return flag


# User Stroy 13, Sibling birth spacing
def us13(indi, fam, f):
    flag = True
    print("User Story 13 - Siblings spacing, running")
    for family in fam:
        if family["CHIL"] is "NA" or len(family["CHIL"]) is 1:
            continue
        len_children = len(family["CHIL"])
        for x in range(len_children):
            child1 = getIndiByID(indi, family["CHIL"][x])

            for child_2_Index in range(x + 1, len_children):
                child2 = getIndiByID(indi, family["CHIL"][child_2_Index])
                difference = (child1["BIRT"] - child2["BIRT"]).days.__abs__()
                if 2 < difference and difference > 243.334:
                    continue
                else:
                    print(f'Error: FAMILY: US13: child ({child1["INDI"]}) and child ({child2["INDI"]}) are born '
                          f'inside 2 days to 8 months of one another')
                    f.write(f'Error: FAMILY: US13: children ({child1["INDI"]}) and ({child2["INDI"]}) are born '
                            f'inside 2 days to 8 months of one another')
                    flag = False

    print("User Story 13 Completed")
    return flag


# User Story 18, siblings should not marry each other
def us18(indi, fam, f):
    flag = True
    print("User Story 18 - Siblings should not marry each other, running")
    for family in fam:
        husb = getIndiByID(indi, family["HUSB"])
        wife = getIndiByID(indi, family["WIFE"])
        if husb["FAMC"] == wife["FAMC"] and husb["FAMC"] != "NA" and wife["FAMC"] != "NA":
            print(f'Error: FAMILY: US18: spouses {family["HUSB"]} and {family["WIFE"]} are siblings')
            f.write(f'Error: FAMILY: US18: spouses {family["HUSB"]} and {family["WIFE"]} are siblings')
            flag = False

    print("User Story 18 Completed")
    return flag


# User Story 23, unique name and birthdate
# No more than one individual with the same name and birth date should appear in a GEDCOM file
def us23(indi, fam, f):
    flag = True
    print("User Story 23 - unique name and birthdate, running")
    people = set()
    for individual in indi:
        if (individual["NAME"], individual["BIRT"]) in people:
            print(
                f'Error: INDIVIDUAL: US23: multiple people with the name {individual["NAME"]} and birthdate {individual["BIRT"]} exist')
            f.write(
                f'Error: INDIVIDUAL: US23: multiple people with the name {individual["NAME"]} and birthdate {individual["BIRT"]} exist')
            flag = False
        else:
            people.add((individual["NAME"], individual["BIRT"]))
    print("User Story 23 Completed")
    return flag


# User Story 28, order siblings by age
# List siblings in families by decreasing age, i.e. oldest siblings first
def us28(indi, fam, f):
    print("User Story 28 - order siblings by age, running")
    output = list()
    for family in fam:
        children_Ids = family["CHIL"]
        if 0 <= len(children_Ids) < 2 or children_Ids == "NA":
            continue

        children_dicts = list()
        for i in children_Ids:
            child = getIndiByID(indi, i)
            details = (child["NAME"], child["BIRT"])
            children_dicts.append(details)

        children_dicts = sorted(children_dicts, key=lambda j: j[1])
        output.append(children_dicts)

    print("User Story 28 Completed")
    return output


# User Story 33, List orphans
# List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
def us33(indi, fam, f):
    print("User Story 33 - List orphans, running")
    orphans = list()
    for family in fam:
        husb = getIndiByID(indi, family["HUSB"])
        wife = getIndiByID(indi, family["WIFE"])
        if husb["DEAT"] == "NA" or wife["DEAT"] == "NA":
            continue

        # both parents are dead
        children_ids = family["CHIL"]
        if children_ids == "NA":
            continue

        for i in children_ids:
            child = getIndiByID(indi, i)
            if child["DEAT"] != "NA":
                continue

            # child is alive
            if int(calculateage(child["BIRT"], "NA")) < 18:
                orphans.append(child)

    print("User Story 33 Completed")
    return orphans


# US38
# List upcoming birthdays
# List all living people in a GEDCOM file whose birthdays occur in the next 30 days
def us38(indi, fam, f):
    print("User Story 38 - List upcoming birthdays, running")
    upcoming_birthdays = list()
    for individual in indi:
        if individual["DEAT"] != "NA":
            continue

        # isAlive
        todays_date = datetime.today()
        birth_day = individual["BIRT"]
        birth_day = birth_day.replace(year=todays_date.year)

        if 0 < (birth_day - todays_date).days <= 30:
            upcoming_birthdays.append(individual)

    print("User Story 33 Completed")
    return upcoming_birthdays


# helper function 1
def getIndiByID(indi, iD):
    return next((dictionary for dictionary in indi if dictionary['INDI'] == iD), None)


# helper function 2
def getFamByID(fam, iD):
    return next((dictionary for dictionary in fam if dictionary["FAM"] == iD), None)
