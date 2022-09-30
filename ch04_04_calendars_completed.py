#
# Learning in Tamil - Python 
# Example file - Calendars
#

import calendar

# How to create a plain text calendar
textCalendar = calendar.TextCalendar(calendar.MONDAY)
calendarString = textCalendar.formatmonth(2022, 10)
print (calendarString)

# How to create a HTML calendar
htmlCalendar = calendar.HTMLCalendar(calendar.MONDAY)
calendarString = htmlCalendar.formatmonth(2022, 10)
print (calendarString)

# iterate days of a month
for dateVal in textCalendar.itermonthdays(2022, 8):
    print (dateVal)
  
# names of days
for dayName in calendar.day_name:
    print (dayName)
# names of months
for month in calendar.month_name:
    print (month)

# Calculate project meeting days
print ("Project meetings will be on:")
for month in range(1,13):
    monthArray = calendar.monthcalendar(2022, month)
    firstWeek = monthArray[0]
    secondWeek = monthArray[1]
    #print(firstWeek)
    #print(secondWeek)
    if firstWeek[calendar.MONDAY] != 0:
        meetingday = firstWeek[calendar.MONDAY]
    else:
        meetingday = secondWeek[calendar.MONDAY]
      
    print ("%10s %2d" % (calendar.month_name[month], meetingday))
