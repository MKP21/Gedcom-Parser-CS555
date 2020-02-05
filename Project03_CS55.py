# CS 555-A, Project 02
# Submitted by: Meet Patel, cwid: 10446501
# Date: 2 Feb 2020
# please select the file by inserting name here


# reading the file and printing output
def main() -> None:
    f = open("Project01.ged", "r")
    obj = None
    currtag = None  # flag to signal which object is being processed
    indi = ()  # list of INDI objects
    fam = ()  # list of FAM objects

    for line in f:
        elems = line.split()
        v = isvalid(elems)
        if v is None:
            print(f' {line} is invalid')
            continue

        # the line is valid
        if v[0] is '0' and (v[1] is 'FAM' or v[1] is 'INDI'):
            if currtag is not None:
                # check validity of the existing object
                # ideally will call functions defined in the INDI and FAM classes to check for user stories
                print('check for object validity and save it, also make the variable pointing to the object as None')

            # set the flag to new object value
            currtag = v[1]
        elif v[0] is '0':
            continue

        # use currtag to call function to create the appropriate object
        if currtag == 'FAM':
            print('')
            # call appropriate function
        elif currtag is 'INDI':
            print("")
            # call appropriate function

        print(v)
    f.close()


# Function to check the validity of the line
def isvalid(parser):
    lvlonetags = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', "MARR", 'HUSB', 'WIFE', 'CHIL', 'DIV')
    lvlzero = ('HEAD', "TRLR", 'NOTE')
    lvlidentity = ('FAM', 'INDI')
    lvltwotags = 'DATE'

    level = parser[0]
    tag = parser[1]
    val = 'N'
    args = ' '.join(parser[2:])
    # check for tag IND or FAM separately
    if level == '0' and parser[1] == lvlzero:
        val = 'Y'
    elif level == '0' and parser[2] in lvlidentity:
        tag = parser[2]
        args = parser[1]
        val = 'Y'
    elif level == '1' and parser[1] in lvlonetags:
        val = 'Y'
    elif level == '2' and parser[1] in lvltwotags:
        val = 'Y'
    # end of else
    if val == 'N':
        return None
    else:
        return level, tag, args


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
