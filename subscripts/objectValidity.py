# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import DatebeforeCurrentDate
from subscripts.userStories.UserStories_Pratik_Deo import MarriageAfter14
from subscripts.userStories.UserStories_MP import us3, us8
from subscripts.userStories.UserStories_MD import us04, us07
from subscripts.userStories.UserStories_DK import us2, us9
from subscripts.userStories.UserStories_AS import us05,us06


def objectvalid(indi, fam):
    f = open("Output_Project", "w")
    DatebeforeCurrentDate(indi, fam, f)
    us2(indi, fam, f)
    us3(indi, fam, f)
    us04(indi, fam, f)
    us05(indi, fam, f)
    us06(indi, fam, f)
    us07(indi, fam, f)
    us8(indi, fam, f)
    us9(indi, fam, f)
    MarriageAfter14(indi, fam, f)

    return True
