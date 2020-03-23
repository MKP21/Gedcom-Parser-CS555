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
                        f.write(
                            f"ERROR: INDIVIDUAL : US05 : {individuals['INDI']} : Married {families['MARR']} after husband's ({individuals['INDI']}) death on {individuals['DEAT']} \n")
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


def us11(indi, fam, f):
    print("User Story 11 - Marriage should not occur during marriage to another spouse, Running")
    flag = True
    for individual in indi:
        if individual["FAMS"] != 'NA':
            if len(individual["FAMS"]) > 1:
                spouse = list()
                for sp in individual["FAMS"]:
                    s = getFamByID(fam, sp)
                    spouse.append(s)
                for sp1 in spouse:
                    check = sp1['DIV']
                    for sp2 in spouse:
                        if sp1 != sp2:
                            if sp2["MARR"] != 'NA':
                                if check != 'NA':
                                    if sp1["MARR"] < sp2["MARR"]:
                                        if sp2["MARR"] < check:
                                            f.write(
                                                f"ERROR: FAMILY : US11 : {individual['INDI']} : Individual is in mutliple families at once  \n")
                                            flag = False
                if individual["SEX"] == 'F':
                    spouse2 = list()
                    for sp3 in individual["FAMS"]:
                        s = getFamByID(fam, sp3)
                        infoindi = getIndiByID(indi, s["HUSB"])
                        spouse2.append(infoindi)
                    for sp1 in spouse:
                        for sp2 in spouse2:
                            if sp1["HUSB"] != sp2["INDI"]:
                                if sp2["DEAT"] != 'NA':
                                    if sp1["MARR"] < sp2["DEAT"]:
                                        f.write(
                                            f"ERROR: FAMILY : US11 : {individual['INDI']} : Individual is in mutliple families at once  \n")
                                        flag = False
                if individual["SEX"] == 'M':
                    spouse2 = list()
                    for sp3 in individual["FAMS"]:
                        s = getFamByID(fam, sp3)
                        infoindi = getIndiByID(indi, s["WIFE"])
                        spouse2.append(infoindi)
                    for sp1 in spouse:
                        for sp2 in spouse2:
                            if sp1["WIFE"] != sp2["INDI"]:
                                if sp2["DEAT"] != 'NA':
                                    if sp1["MARR"] < sp2["DEAT"]:
                                        f.write(
                                            f"ERROR: FAMILY : US11 : {individual['INDI']} : Individual is in mutliple families at once  \n")
                                        flag = False
    print("User Story 11 Completed")
    return flag


def us20(indi, fam, f):
    print("User Story 20 - Aunts and Uncles should not marry their nieces and nephews , Running")
    flag = True
    for individual in indi:
        if individual["FAMC"] == "NA" or individual["FAMS"] == "NA":
            continue
        # get parents of spouses for an individual
        parents_of_spouses = list()
        spouse_gender = "HUSB"
        if individual["SEX"] == "M":
            spouse_gender = "WIFE"
        for family_id in individual["FAMS"]:
            family = getFamByID(fam, family_id)
            spouse = getIndiByID(indi, family[spouse_gender])
            if spouse["FAMC"] == "NA":
                continue
            else:
                famc_spouse = getFamByID(fam, spouse["FAMC"][0])
                parents_of_spouses.append((spouse["INDI"], famc_spouse["HUSB"]))
                parents_of_spouses.append((spouse["INDI"], famc_spouse["WIFE"]))
        if len(parents_of_spouses) == 0:
            continue

        # for an individual check in "FAMC", if siblings are present as parents of spouses
        famc_individual = getFamByID(fam, individual["FAMC"][0])
        for child in famc_individual["CHIL"]:
            if child == individual["INDI"]:
                continue
            for spouse, parent in parents_of_spouses:
                if child == parent:
                    flag = False
                    print(f"Error: US 20 Individual {spouse} has married their aunt/uncle {individual['INDI']}")
                    f.write(f"Error: US 20 Individual {spouse} has married their aunt/uncle {individual['INDI']}")

    print("User Story 20 Completed")
    return flag
