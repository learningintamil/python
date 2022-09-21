#
# Learning in Tamil - Python 
# Example file - formatting time and date
#

from datetime import datetime

def main():
    # Get current date and time using datetime
    currentDateTime = datetime.now()
    # Format the date time
    print (currentDateTime.strftime("Current year: %Y")) #year
    print (currentDateTime.strftime("Current year: %y")) #abbreviated year

    print (currentDateTime.strftime("Month: %B")) #month
    print (currentDateTime.strftime("Month: %b")) #abbreviated

    print (currentDateTime.strftime("Date: %d")) #date
    
    print (currentDateTime.strftime("Weekday: %A")) #weekday
    print (currentDateTime.strftime("Weekday: %a")) #abbreviated weekday
    
    
    print (currentDateTime.strftime("Locale date: %x"))
    print (currentDateTime.strftime("Locale time: %X"))

    # find locale timezone
    print(currentDateTime.astimezone().tzinfo.tzname(currentDateTime))
    print (currentDateTime.strftime("Locale date and time: %c"))

    # Format the time
    print (currentDateTime.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
    print (currentDateTime.strftime("24-hour time: %H:%M")) # 24-Hour:Minute

if __name__ == "__main__":
    main()
