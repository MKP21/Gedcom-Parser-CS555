# import pretty table for displaying output in Prettytable format
# keep prettytable module files in the same folder as the file importing it


def outputtable(indi, fam):
    import prettytable
    import datetime

    itable = prettytable.PrettyTable()
    # adding fieldnames
    itable.field_names = ["ID", "NAME", "GENDER", "BIRTHDAY", "AGE", "ALIVE", "DEATH", "CHILD", "SPOUSE"]

    # creating text file
    newf = open('indiOutput_Project_03.txt', 'w')
    newf.write(f'{" ".join(["ID", "NAME", "GENDER", "BIRTHDAY", "AGE", "ALIVE", "DEATH", "CHILD", "SPOUSE"])} \n')

    # adding data
    for item in indi:
        newrow = [item["INDI"],
                  item["NAME"],
                  item["SEX"],
                  item["BIRT"] if item["BIRT"] == "NA" else item["BIRT"].strftime("%d %b %Y"),
                  calculateage(item["BIRT"], item["DEAT"]),
                  "TRUE" if item["DEAT"] == "NA" else "FALSE",
                  item["DEAT"] if item["DEAT"] == "NA" else item["DEAT"].strftime("%d %b %Y"),
                  str(item["FAMC"]),
                  str(item["FAMS"])]
        itable.add_row(newrow)
        newf.write(f"{' '.join(newrow)} \n")

    # printing the table
    print(itable)

    newf.close()

    ftable = prettytable.PrettyTable()
    # adding fieldnames
    ftable.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND ID", "HUSBAND NAME", "WIFE ID", "WIFE NAME", "CHILDREN"]

    # creating text file
    newf = open('famOutput_Project_03.txt', 'w')
    newf.write(
        f'{" ".join(["ID", "MARRIED", "DIVORCED", "HUSBAND ID", "HUSBAND NAME", "WIFE ID", "WIFE NAME", "CHILDREN"])} \n')

    # adding data
    for item in fam:
        husbobj = dictsearch(item["HUSB"], indi)
        wifeobj = dictsearch(item["WIFE"], indi)
        newrow = [item["FAM"],
                  item["MARR"] if item["MARR"] == "NA" else item["MARR"].strftime("%d %b %Y"),
                  item["DIV"] if item["DIV"] == "NA" else item["DIV"].strftime("%d %b %Y"),
                  item["HUSB"],
                  "NA" if husbobj is None else husbobj["NAME"],
                  item["WIFE"],
                  "NA" if wifeobj is None else wifeobj["NAME"],
                  str(item["CHIL"])]
        ftable.add_row(newrow)
        newf.write(f"{' '.join(newrow)} \n")

    # printing the table
    print(ftable)
    newf.close()


# calculateage function referred from https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/


def calculateage(birth, death):
    from datetime import date
    latest = date.today()
    if death != "NA":
        latest = death.date()

    days_in_year = 365.2425
    age = int((latest - birth.date()).days / days_in_year)
    return str(age)


def dictsearch(uid, indilist):
    for i in indilist:
        if i["INDI"] == uid:
            return i
