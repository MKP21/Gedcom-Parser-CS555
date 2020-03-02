from datetime import datetime
from datetime import timedelta
from inspect import currentframe

frameinfo = currentframe()


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
                    f"FAMILY: us04 {frameinfo.f_back.f_lineno}: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} ")
                f.write(
                    f"FAMILY: us04 {frameinfo.f_back.f_lineno}: {family['FAM']}: divorce {family['DIV']} before marriage {family['MARR']} ")
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
                    f"INDIVIDUAL: us07: {frameinfo.f_back.f_lineno}: {indv['INDI']}: death {indv['DEAT']} after 150 years")
                f.write(
                    f"INDIVIDUAL: us07: {frameinfo.f_back.f_lineno}: {indv['INDI']}: death {indv['DEAT']} after 150 years")
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
                    f"ERROR: INDIVIDUAL: us07: {frameinfo.f_back.f_lineno}: {indv['INDI']}: birth {indv['DEAT']} before 150 years from current date {cd}")
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
                print(
                    f"family with id {families['FAM']}has more than 5 siblings who were born on the same date and time")
                flag = False
    # End of for loop

    if flag:
        print("User Story 14 Completed")
        return True
    else:
        print("User Story 14 Completed")
        return False

