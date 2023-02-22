'''Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904'''
from math import *
def degr_rad(degr):
    return round(degr*pi/180,6)

if __name__== "__main__":
    deg = int(input("write degree: "))

print("in radian: ",degr_rad(deg))