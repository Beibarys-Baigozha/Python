'''Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625   '''
from math import *
from degree_to_radian import degr_rad

if __name__== "__main__":
    def areaPol(n, a):
        rad = degr_rad(180/n)
        return round((n*(a**2))/(4*tan(rad)), 2)

    n = int(input("Input number of sides: "))
    l = int(input("Input the length of a side: "))

print("The area of the polygon is: ", areaPol(n, l))