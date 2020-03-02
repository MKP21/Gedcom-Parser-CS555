from datetime import datetime
from datetime import timedelta

# Birth before death


def us3(indi, fam):
    print("User Story 3 - Birth before death, Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"Error: {person['INDI']} {person['NAME']} were born before they died")

    print("User Story 3 Completed")
    return True


# Birth before marriage of parent
def us8(indi, fam):
    print("User Story 8 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        if family["CHIL"] is "NA":
            continue
        for child in family["CHIL"]:
            childobj = next(
                (item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                if family["DIV"] != "NA" and childobj["BIRT"] > family["DIV"] + timedelta(days=273.93188):
                    print(f"Error: Indi id -> {childobj['INDI']}, Birth after divorce of parents")
                    return False
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Error: Indi id -> {childobj['INDI']}, Birth before marriage of parents")
                return False
            else:
                print(f'Error: child with id {child} does not exist in indi list')
                return False

    print("User Story 8 Completed")
    return True