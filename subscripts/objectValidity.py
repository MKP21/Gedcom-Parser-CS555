# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import us01, us10
from subscripts.userStories.UserStories_MP import us03, us08, us13, us18
from subscripts.userStories.UserStories_MD import us04, us07
from subscripts.userStories.UserStories_DK import us02, us09
from subscripts.userStories.UserStories_AS import us05, us06


def objectvalid(indi, fam):
    f = open("Output_Project.txt", "a")
    f.write("\n \n")
    us01(indi, fam, f)
    us02(indi, fam, f)
    us03(indi, fam, f)
    us04(indi, fam, f)
    us05(indi, fam, f)
    us06(indi, fam, f)
    us07(indi, fam, f)
    us08(indi, fam, f)
    us09(indi, fam, f)
    us10(indi, fam, f)
    us13(indi, fam, f)
    us18(indi, fam, f)
    f.close()
    return True
