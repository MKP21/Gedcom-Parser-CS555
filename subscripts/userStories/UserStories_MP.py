from datetime import datetime
from datetime import timedelta


# Birth before death


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
                    print(f" Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of parents")
                    f.write(f"Error: INDIVIDUAL: US08: id -> {childobj['INDI']}, Birth 9 months after divorce of "f"parents \n")
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


# helper function 1
def getIndiByID(indi, iD):
    return next((dictionary for dictionary in indi if dictionary['INDI'] == iD), None)


# helper function 2
def getFamByID(fam, iD):
    return next((dictionary for dictionary in fam if dictionary["FAM"] == iD), None)
