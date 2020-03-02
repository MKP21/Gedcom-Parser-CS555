# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import DatebeforeCurrentDate
from subscripts.userStories.UserStories_Pratik_Deo import MarriageAfter14
from subscripts.userStories.UserStories_MP import us3, us8
from subscripts.userStories.UserStories_MD import us4, us7, us14
from subscripts.userStories.UserStories_DK import us02, us09
from subscripts.userStories.UserStories_AS import us05, us06


def objectvalid(indi, fam):
    f = open("Output_Project.txt", "a")
    f.write("\n \n")
    DatebeforeCurrentDate(indi, fam, f)
    us02(indi, fam, f)
    us3(indi, fam, f)
    us4(indi, fam, f)
    us05(indi, fam, f)
    us06(indi, fam, f)
    us7(indi, fam, f)
    us8(indi, fam, f)
    us09(indi, fam, f)
    MarriageAfter14(indi, fam, f)

    return True
