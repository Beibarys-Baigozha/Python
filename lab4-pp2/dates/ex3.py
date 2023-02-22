'''Write a Python program to drop microseconds from datetime.'''
import datetime

date = datetime.datetime.today().replace(microsecond=0,)
print(date)