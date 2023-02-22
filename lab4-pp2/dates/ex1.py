'''Write a Python program to subtract five days from current date.'''
import datetime

crntDate = datetime.datetime.today()
day = crntDate.day - 5 
date = datetime.date(crntDate.year,crntDate.month,day)
print(date)