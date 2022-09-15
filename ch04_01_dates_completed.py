#
# Learning in Tamil - Python 
# Example file - working with date
#

from datetime import date
from datetime import datetime

def main():
    #DATE
    # Get today's date using DATE
    currentDate = date.today()
    print("Current date: ", currentDate)
    #components in date
    print ("Day: ", currentDate.day, " Month: ", currentDate.month, "Year: ", currentDate.year) 
    
    # get weekday
    print ("Day of a week: ", currentDate.weekday())

    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print ("Today is: ", weekdays[currentDate.weekday()])
    
    #DATETIME
    #How to get today's date using DATETIME
    currentDateTime = datetime.now()
    print  ("Current date and time: ", currentDateTime)

    #How to get current time
    currentTime = datetime.time(currentDateTime)
    print("current time: ", currentTime) 
  
if __name__ == "__main__":
    main()
