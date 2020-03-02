from datetime import datetime
from datetime import timedelta


# Birth before death


def us03(indi, fam, f):
    flag = True
    print("US 03 - Birth before death, Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} were born before they died")
            f.write(f"Error: INDIVIDUAL: US02: {person['INDI']} {person['NAME']} were born before they died \n")
            flag = False

    print("US 03 Completed")
    return flag


# Birth before marriage of parent
def us08(indi, fam, f):
    flag = True
    print("US 08 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        if family["CHIL"] is "NA":
            continue
        for child in family["CHIL"]:
            childobj = next((item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                if family["DIV"] != "NA" and childobj["BIRT"] > family["DIV"] + timedelta(days=273.93188):
                    print(
                        f" Error: INDIVIDUAL: US02: id -> {childobj['INDI']}, Birth after divorce of parents")
                    f.write(
                        f"Error: INDIVIDUAL: US02: id -> {childobj['INDI']}, Birth after divorce of parents \n")
                    falg = False
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Error: INDIVIDUAL: US02: id -> {childobj['INDI']}, Birth before marriage of parents")
                f.write(f"Error: INDIVIDUAL: US02: -> {childobj['INDI']}, Birth before marriage of parents \n")
                flag = False
            else:
                print(f'Error: INDIVIDUAL: US02: child with id {child} does not exist in indi list')
                f.write(f"Error: INDIVIDUAL: US02:child with id {child} does not exist in indi list \n")
                flag = False

    print("US 08 Completed")
    return flag;
