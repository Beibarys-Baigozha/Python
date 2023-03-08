'''Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858'''
import time
import math

def specSqrt(number, mlscnd):
    time.sleep(mlscnd/1000)
    return math.sqrt(num)

num = int(input("write squared number:"))
milisec = int(input("write milisecond:"))

print(f"Square root of {num} after {milisec} miliseconds is {specSqrt(num, milisec)}")