'''Write a python program to convert snake 
case string to camel case string.'''
import re

snake_case = input()
x = re.split("_",snake_case)
camelCase = ""

for i in x:
    camelCase += i.capitalize()
print(camelCase)