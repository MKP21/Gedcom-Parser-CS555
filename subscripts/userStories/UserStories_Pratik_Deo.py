from datetime import date
from subscripts.outputDisplay import calculateage


today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def us01(indi, fam , f):
    print("US 01 - all dates should be before current date, Running")
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            pass
        elif i["DEAT"].date() > today:
            print("US 01 Error indi id ->" + str(i["INDI"]) + str(i["DEAT"]))
            f.write(f"Error: INDIVIDUAL: US01: Date before Current Date" + str(i["INDI"]) + " "+str(i["DEAT"])+"\n")
            return False

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            pass
        elif i["BIRT"].date() > today:
            print("These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))
            f.write(f"Error: INDIVIDUAL: US01: Birth date after current date" + str(i["INDI"])+ " "+str(i["NAME"]) +" "+ str(i["BIRT"].date()) +"\n")
            return False

    for j in fam:

        if j["MARR"].date() > today:
            print("Error: INDIVIDUAL: US01: Marriage date after current date " + str(j["MARR"].date()) + " " + str(today))
            return False

        if str(j["DIV"]) == "NA":
            pass
        elif j["DIV"].date() > today:
            print("Error: INDIVIDUAL: US01: Divorce date after current date " + str(j["DIV"].date()) +" " + str(today))
            return False
    
    print("US 01 completed ")
    return True 
    

# User story 10 - Marriage should be after 14 years of age
def us10(indi, fam, f):
    print("US 10 - Marriage should be after 14 years of age, Runnning")
    
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"]))
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) +" "+ str(j["MARR"]))
                    return False

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"])) 
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) +" "+ str(j["MARR"]))
                    return False                
    
    print("US 10 completed ")
    return True 
    

#Helper functions
def getLastNamebyId(indi, Id):
    for i in indi:
        list1= []
        if(i["INDI"] == Id):
            s = i["NAME"]
            #print(s)
            list1 = s.split()
            return list1[1]

def getSexByid(indi, Id):
    sex = ""
    for i in indi:
        if(i["INDI"] == Id):
            sex = i["SEX"]
            
    return sex

def getAgeById(indi, Id):
    age = 0
    for i in indi:
        if(i["INDI"] == Id ):
            age = calculateage(i["BIRT"], i["DEAT"])
    
    return age

def getAliveById(indi, Id):
    alive = True
    for i in indi:
        if(i["DEAT"] == "NA"):
            alive = True
        else: 
            alive = False
    
    return alive

def getNamebyId(indi, Id):
    name = " "
    for i in indi:
        if(i["INDI"] == Id):
            name = i["NAME"]

    return name