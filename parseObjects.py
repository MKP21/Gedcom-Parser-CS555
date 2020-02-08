# script with functions to create and edit FAM, INDI JSON objects
from collections import OrderedDict
# obj will be referencing to the object being parsed at a given moment
# v will be a list with { level, tag, args } format


def inddetails(obj, v):
    if obj is None:
        # create a new INDI Dict, v[1] will be "INDI" in this line
        obj = OrderedDict({
            "INDI": v[2],
            "NAME": "NA",
            "SEX": "NA",
            "BIRT": "NA",   # date
            "DEAT": "NA",   # date
            "FAMC": "NA",   # array to check possible errors
            "FAMS": "NA"    # array to check possible errors
        })
        return obj
    # end of if
    if v[1] in ("FAMC", "FAMS"):
        if obj[v[1]] == "NA":
            obj[v[1]] = list()
        obj[v[1]].append(v[2])

    elif v[1] in ("BIRT", "DEAT"):
        if obj[v[1]] == "NA":
            obj[v[1]] = None
        else:
            print(f" {v[1]} second birth")
            obj[v[1]] = None

    elif v[1] == "DATE":
        if obj["DEAT"] is None:
            # convert date to string
            obj["DEAT"] = v[2]
        elif obj["BIRT"] is None:
            # convert date to string
            obj["BIRT"] = v[2]
        else:
            print()

    # other tags : INDI, NAME, SEX
    else:
        obj[v[1]] = v[2]
    # end of if

    return obj


def famdetails(obj, v):
    if obj is None:
        # create a new FAM Dict, v[1] will be "FAM" in this line
        obj = OrderedDict({
            "FAM": v[2],
            "HUSB": "NA",
            "WIFE": "NA",
            "CHIL": "NA",
            "MARR": "NA",
            "DIV": "NA",
        })
        return obj
    # end of if
    if v[1] == "CHIL":
        if obj["CHIL"] == "NA":
            obj["CHIL"] = list()
        obj["CHIL"].append(v[2])
    elif v[1] in ("DIV", "MARR"):
        if obj[v[1]] == "NA":
            obj[v[1]] = None
        else:
            print(f"Error: {v} second marriage in same family")
            obj[v[1]] = None
    elif v[1] == "DATE":
        if obj["DIV"] is None:
            # convert date to string
            obj["DIV"] = v[2]
        elif obj["MARR"] is None:
            # convert date to string
            obj["MARR"] = v[2]
        else:
            print(f"Error with date {v}")
    else:
        obj[v[1]] = v[2]

    return obj
