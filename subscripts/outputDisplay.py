# import pretty table for displaying output in Prettytable format
# keep prettytable module files in the same folder as the file importing it


def outputtable(indi, fam):
    import prettytable
    import datetime

    itable = prettytable.PrettyTable()
    # adding fieldnames
    itable.field_names = ["ID", "NAME", "GENDER", "BIRTHDAY", "AGE", "ALIVE", "DEATH", "CHILD", "SPOUSE"]

    # adding data
    for item in indi:
        itable.add_row([item["INDI"],
                        item["NAME"],
                        item["SEX"],
                        item["BIRT"] if item["BIRT"] == "NA" else item["BIRT"].date(),
                        calculateage(item["BIRT"], item["DEAT"]),
                        "TRUE" if item["DEAT"] == "NA" else "FALSE",
                        item["DEAT"] if item["DEAT"] == "NA" else item["DEAT"].date(),
                        item["FAMC"],
                        item["FAMS"]])

    # printing the table
    print(itable)

    ftable = prettytable.PrettyTable()
    # adding fieldnames
    ftable.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND ID", "HUSBAND NAME", "WIFE ID", "WIFE NAME", "CHILDREN"]

    # adding data
    for item in fam:
        husbobj = dictsearch(item["HUSB"], indi)
        wifeobj = dictsearch(item["WIFE"], indi)
        ftable.add_row([item["FAM"],
                        item["MARR"] if item["MARR"] == "NA" else item["MARR"].date(),
                        item["DIV"] if item["DIV"] == "NA" else item["DIV"].date(),
                        item["HUSB"],
                        "NA" if husbobj is None else husbobj["NAME"],
                        item["WIFE"],
                        "NA" if wifeobj is None else wifeobj["NAME"],
                        item["CHIL"]])

    # printing the table
    print(ftable)

# calculateage function referred from https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/


def calculateage(birth, death):
    from datetime import date
    latest = date.today()
    if death != "NA":
        latest = death.date()

    days_in_year = 365.2425
    age = int((latest - birth.date()).days / days_in_year)
    return age


def dictsearch(uid, indilist):
    for i in indilist:
        if i["INDI"] == uid:
            return i
