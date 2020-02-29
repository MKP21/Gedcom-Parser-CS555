from datetime import datetime
from datetime import timedelta


# Birth before Marriage
def us2(indi, fam):
    print("User Story 2 - Birth before Marriage, Running")
    for families in fam:
        for person in indi:
            if families['HUSB'] == person['INDI'] or families['WIFE'] == person['INDI']:
                if person['BIRT'] == 'NA':
                    print("NO BIRTHDATE FOUND")
                m = person['BIRT']
                if families['MARR'] < m:
                    print(
                        f"{person['INDI']} {person['NAME']} were married before birth")

    print("User Story 2 Completed")
    return True

# Birth before death of parents


def us9(indi, fam):
    print("User Story 9 - Birth before death of parents, Running")
    for family in fam:
        fatherdeath = 'NA'
        motherdeath = 'NA'
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

                    if childobj["BIRT"] > motherdeath or childobj["BIRT"] > fatherdeath:
                        print(
                            f"Indi id -> {childobj['INDI']}, Birth before death of parents")
                        return False

    print("User Story 9 Completed")
    return True
