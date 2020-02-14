from datetime import datetime


# Birth before death
def us2(indi, fam):
    print("User Story 2 Running")
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(f"{person['INDI']} {person['NAME']} were born before they died")

    print("User Story 2 Completed")
