'''Write a Python program to print yesterday, today, tomorrow.'''
import datetime

crntDate = datetime.datetime.today()
yday = crntDate.day - 1
tmrwDay = crntDate.day + 1
ydayDate = datetime.date(crntDate.year,crntDate.month,yday)
todayDate = datetime.date(crntDate.year,crntDate.month,crntDate.day)
tmrwDate = datetime.date(crntDate.year,crntDate.month,tmrwDay)

print("Yesterday: ", ydayDate)
print("Today: ", todayDate)
print("Tomorrow: ", tmrwDate)