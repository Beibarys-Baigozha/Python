'''Write a Python program to calculate two date difference in seconds.'''
import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2004,1,27,23,31,36)

diff = (date1-date2).total_seconds()
print(diff)