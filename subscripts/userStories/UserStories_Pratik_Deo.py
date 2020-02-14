from datetime import date

today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def DatebeforeCurrentDate(indi, fam):
    print("user story 1 - all dates should be before current date")
    print(" ")
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            print(" These people are still alive: " + str(i["NAME"]) + str(i["BIRT"].date()))
            print(" ")
        elif i["DEAT"].date() > today:
            print(" Wrong death dates ")
            print(" ")

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            print(" Not Applicable or Missing Birth date")
            print(" ")
        elif i["BIRT"].date() > today:
            print(" These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))
            print(" ")

    for j in fam:

        if j["MARR"].date() > today:
            print(" Marriage date " + str(j["MARR"].date()) + " cannot be after current date " + str(today))
            print(" ")

        if str(j["DIV"]) == "NA":
            print(" Divorce date not applicable ")
            print(" ")
        elif j["DIV"].date() > today:
            print("Divorce date " + str(j["DIV"].date()) + " cannot be after the current date " + str(today))


# User story 10 - Marriage should be after 14 years of age
def MarriageAfter14(indi, fam):
    print("user story 10 - Marriage should be after 14 years of age")
    print(" ")
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    print(str(i["NAME"]) + " was " + str(age) + " years old when married")
                    print(" ")
                else:
                    print("Invalid marriage date ")
                    print(" ")

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    print(str(i["NAME"]) + " was " + str(age) + " years old when married")
                    print(" ")
                else:
                    print("Invalid marriage date ")
                    print(" ")
