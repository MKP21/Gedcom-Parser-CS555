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
                print(f"No marraiage date found in family with id {family['FAM']}")

            if div < marr:
                print(f"Family with id {family['FAM']} has divorce before marriage")

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
                print(f"person with name {indv['NAME']} and id {indv['INDI']} is more than 150 years from birth")
    # End of for loop
    print("User Story 7 Completed")
    return True
