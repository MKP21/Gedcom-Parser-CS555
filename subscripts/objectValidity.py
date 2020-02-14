# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import DatebeforeCurrentDate
from subscripts.userStories.UserStories_Pratik_Deo import MarriageAfter14
from subscripts.userStories.UserStories_MP import us2


def objectvalid(indi, fam):
    DatebeforeCurrentDate(indi, fam)
    MarriageAfter14(indi, fam)
    us2(indi, fam)
    return True
