'''Write a Python program to convert a given 
camel case string to snake case.'''
import re

text = input()
list = list()
x = re.findall('[A-Z][a-z]*', text)

for i in x:
    list.append(i.lower())
r = "_".join(list)
print(r)