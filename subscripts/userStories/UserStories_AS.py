from datetime import datetime


# Marriage before death
def us05(indi, fam):
    print("User Story 5 - Marriage before death, Running")
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband individual
                m = individuals['DEAT']
                # If individual's death date is not null
                if m != 'NA':
                    #checking for marriage date greater than the individual's death date
                    if families['MARR'] > m:
                        print("Marriage before death")
            
            elif families['WIFE'] == individuals['INDI']:
                # getting death date for wifi individual
                n = individuals['DEAT']
                 # If individual's death date is not null
                if n!= 'NA':
                    #checking for marriage date greater than the individual's death date
                    if families['MARR'] > n:
                        print("Marriage before death")


  
    print("User Story 5 Completed")
    return True

# Divorce before death
def us06(indi, fam):
    print("User Story 6 - Divorce before death, Running")
    for families in fam:
        for individuals in indi:
            # checking for husband id is equal to individual id
            if families['HUSB'] == individuals['INDI']:
                # getting death date for husband individual
                m = individuals['DEAT']
                if m != 'NA' and families['DIV'] !='NA':
                    if m < families['DIV']:
                        print("Divorce before death")
            
            if families['WIFE'] == individuals['INDI']:
                n = individuals['DEAT']
                if n!= 'NA' and families['DIV'] !='NA':
                    if n < families['DIV']:
                        print("Divorce before death")


  
    print("User Story 6 Completed")
    return True