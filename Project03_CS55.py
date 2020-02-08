# CS 555-A, Project 02
# Submitted by: Meet Patel, cwid: 10446501
# Date: 2 Feb 2020
from objectValidity import objectvalid
from parseObjects import inddetails, famdetails
from lineValidity import isvalid


def main() -> None:
    # please select the file by inserting name here
    f = open("Project01.ged", "r")

    obj = None  # refers to the Dict/JSON object being parsed at a given moment
    currtag = None  # Type of object (FAM, INDI) being processed
    indi = list()  # list of INDI objects
    fam = list()  # list of FAM objects

    for line in f:
        elems = line.split()
        v = isvalid(elems)  # if line is valid it returns a list of level,tag,args, else returns None
        if v is None:
            # print(f' {line} is invalid')
            continue
        else:
            # print(v)
            None
        # the line is valid

        if v[0] is '0' and (v[1] in ('FAM', 'INDI')):
            if currtag is not None:
                # check object validity
                if objectvalid(obj):
                    if 'INDI' in obj:
                        indi.append(obj)
                    else:
                        fam.append(obj)
                # end of if
                obj = None

            # set the currtag flag to the new tag being parsed
            currtag = v[1]

        elif v[0] is '0':
            # NOTE, TRLR, HEAD
            continue

        # use currtag to call function to create the appropriate JSON/Dict object
        if currtag == 'FAM':
            obj = famdetails(obj, v)
        elif currtag == 'INDI':
            obj = inddetails(obj, v)
        elif obj is None:   # the first valid line is not a FAM or IND
            currtag = None
    # end of for

    f.close()

    print(indi)
    print(fam)


if __name__ == "__main__":
    main()

# read line
# check for validity, else "read next line"
# if level is 0 then we will check the class variable (IND or FAM or None)
#       if tag is None (first object)
#           set class variable to tag
#       elif tag is already set
#           run validity of object (call to user story tests) before pushing it to the list
#               throw error or push object to list, set object variable to None and set tag to new value
#
#       if tag is IND:
#           initialise IND object if it does not exist, or add the attribute mentioned in this line
#       elif tag is FAM:
#
