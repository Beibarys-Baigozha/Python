'''Write a Python program to find the sequences 
of one upper case letter followed by lower case letters.'''
import re

text = input()
pat = r"[A-Z][a-z]+"
x = re.findall(pat, text)

print(x)