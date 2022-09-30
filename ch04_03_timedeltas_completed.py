#
# Learning in Tamil - Python 
# Example file - timedelta
#

from calendar import month
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# new timedelta object
print (timedelta(weeks=2, days=10, hours=5, minutes=30, seconds=20))

# current date
currentDateTime = datetime.now()
print ("Current Date and Time: " + str(currentDateTime))

# add number of days to current date
print ("200 days from current date: " + str(currentDateTime + timedelta(days=200)))

print ("in 3 weeks and 4 days from current date: " + str(currentDateTime + timedelta(weeks=3, days=4)))

#  2 weeks ago
twoWeeksAgo = datetime.now() - timedelta(weeks=2)
print(str(twoWeeksAgo))
twoWeeksAgoFormatted = twoWeeksAgo.strftime("%A %B %d, %Y")
print ("Two weeks ago it was " + twoWeeksAgoFormatted)

# How many days until Valentine's Day?

today = date.today()  #today
valentinesDay = date(today.year, 2, 14)  #valentine's day

#if the day already passed, replace the year with next year by adding 1 to year.
if valentinesDay < today:
    print ("Valentine's Day already passed by %d days ago" % ((today-valentinesDay).days))
    valentinesDay = valentinesDay.replace(year=today.year + 1)  

# Valentine's Day  
daysTovalentinesDay = valentinesDay - today
print ("You have", daysTovalentinesDay.days, "days until next Valentine's Day!")
