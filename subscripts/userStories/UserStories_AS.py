from datetime import datetime
from subscripts.userStories.UserStories_MP import getIndiByID, getFamByID

# Marriage before death
def us05(indi, fam, f):
    print("User Story 5 - Marriage before death, Running")
    flag = True
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband individual
                m = individuals['DEAT']
                # If individual's death date is not null
                if m != 'NA':
                    # checking for marriage date greater than the individual's death date
                    if families['MARR'] > m:
                        f.write(f"ERROR: INDIVIDUAL : US05 : {individuals['INDI']} : Married {families['MARR']} after husband's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

            # checking for wife id is equal to individual id
            elif families['WIFE'] == individuals['INDI']:
                # getting death date for wifi individual
                n = individuals['DEAT']
                # If individual's death date is not null
                if n != 'NA':
                    # checking for marriage date greater than the individual's death date
                    if families['MARR'] > n:
                        f.write(
                            f"ERROR: INDIVIDUAL : US05 : {individuals['INDI']} : Married {families['MARR']} after wifi's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

    print("User Story 5 Completed")
    return flag


# Divorce before death
def us06(indi, fam, f):
    print("User Story 6 - Divorce before death, Running")
    flag = True
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband's individual
                m = individuals['DEAT']
                # If individual's death date is not null and families divorce date is not null
                if m != 'NA' and families['DIV'] != 'NA':
                    # checking for husband's death date less than the divorces date
                    if m < families['DIV']:
                        f.write(
                            f"ERROR: FAMILY : US06 : {individuals['INDI']} : Divorced {families['DIV']} after husband's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

            # checking for wife id is equal to individual id
            if families['WIFE'] == individuals['INDI']:
                # getting death date for wifi's individual
                n = individuals['DEAT']
                # If individual's death date is not null and families divorce date is not null
                if n != 'NA' and families['DIV'] != 'NA':
                    # checking for wife's death date less than the divorces date
                    if n < families['DIV']:
                        f.write(
                            f"ERROR: FAMILY : US06 : {individuals['INDI']} : Divorced {families['DIV']} after wifi's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
                        flag = False

    print("User Story 6 Completed")
    return flag

def us20(indi, fam, f):
    print("User Story 20 - Aunts and Uncles should not marry their nieces and nephews , Running")
    flag = True
  
    for family in fam:
        if family['CHIL'] and family['CHIL']!='NA':
            if family['HUSB'] in family['CHIL']:
                for family2 in fam:
                    if family2['HUSB'] != family['HUSB'] and fam['HUSB'] in family2['CHIL']:
                        f.write(
                            f"ERROR: FAMILY : US20 : Aunts married   \n")
                        flag = False
            if family['WIFE'] in family['CHIL']:
                for family2 in fam:
                    if family2['WIFE'] != family['WIFE'] and fam['WIFE'] in family2['CHIL']:
                        f.write(
                            f"ERROR: FAMILY : US20 :  \n")
                        flag = False
    print("User Story 20 Completed")
    return flag


def us11(indi, fam, f):
    print("User Story 11 - Marriage should not occur during marriage to another spouse, Running")
    flag = True            
    for individuals in indi:      
        list_t = []
        for family in fam:
                if family['HUSB'] == individuals['INDI']:
                    if family['DIV']:
                        break
                    elif family['HUSB'] in list_t:
                        f.write(
                            f"ERROR: FAMILY : US20 :  \n")
                    else:
                        list_t.append(family['HUSB'])
                if family['WIFE'] == individuals['INDI']:
                    if family['DIV']:
                        break
                    elif family['WIFE'] in list_t:
                        f.write(
                            f"ERROR: FAMILY : US20 :  \n")
                    else:
                        list_t.append(family['WIFE'])

    print("User Story 11 Completed")
    return flag
