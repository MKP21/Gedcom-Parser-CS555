from datetime import datetime
from datetime import timedelta


# Marriage before divorce
def us4(indi, fam):
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
                    f"Family with id {family['FAM']} has divorce before marriage")

    # end of for loop
    print("User Story 4 Completed")
    return True


# Less than 150 years old

def us7(indi, fam):
    print("User Story 7 - Less than 150 years old, Running")
    for indv in indi:
        death = indv['DEAT']
        birth = indv['BIRT']
        # if Death date is defined for the individual
        if death != 'NA':
            no_of_days = (death - birth)
            if no_of_days > timedelta(days=54750):
                print(
                    f"Death of person with name {indv['NAME']} and id {indv['INDI']} is more than 150 years from birth")
        # if Death date is not defined for the individual
        else:
            # current date
            cd = datetime.now()
            no_of_days = cd - birth
            if no_of_days > timedelta(days=54750):
                print(
                    f"person with name {indv['NAME']} and id {indv['INDI']} is more than 150 years from birth")
    # End of for loop
    print("User Story 7 Completed")
    return True

    # Multiple births <= 5


def us14(indi, fam):
    print("User Story 14 - Multiple births <= 5, Running")
    for families in fam:
        if families['CHIL'] == 'NA' or len(families['CHIL']) <= 5:
            continue
        else:
            birthDates = []
            count = 1
            for child in families['CHIL']:
                for indv in indi:
                    if child == indv['INDI']:
                        birthDates.append(indv['BIRT'])

            for sib in range(len(birthDates) - 1):
                if birthDates[sib] == birthDates[sib + 1]:
                    count += 1
            if count > 5:
                print(f"family with id {families['FAM']}has more than 5 siblings who were born on the same date and time")
    # End of for loop
    print("User Story 14 Completed")
    return True
