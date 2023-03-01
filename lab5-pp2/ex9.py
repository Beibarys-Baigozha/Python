'''Write a Python program to insert spaces 
between words starting with capital letters.'''
import re

text = input()
x = re.findall(r'[A-Z][a-z]*', text)
res = ""

for i in x:
    res += i + " "
print(res)