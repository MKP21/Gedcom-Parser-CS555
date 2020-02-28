# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import DatebeforeCurrentDate
from subscripts.userStories.UserStories_Pratik_Deo import MarriageAfter14
from subscripts.userStories.UserStories_MP import us3, us8
from subscripts.userStories.UserStories_MD import us4, us7
from subscripts.userStories.UserStories_DK import us2, us9


def objectvalid(indi, fam):
    DatebeforeCurrentDate(indi, fam)
    MarriageAfter14(indi, fam)
    us2(indi, fam)
    us8(indi, fam)
    us4(indi, fam)
    us7(indi, fam)
    us2(indi, fam)
    us9(indi, fam)
    return True
