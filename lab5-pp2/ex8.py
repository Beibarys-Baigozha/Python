'''Write a Python program to split a string 
at uppercase letters.'''
import re

text = input()
x = re.split(r"[A-Z]", text)

print(x)