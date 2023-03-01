'''Write a Python program to find sequences 
of lowercase letters joined with a underscore.'''
import re

text = input()
pat = r"[a-z]+_[a-z]+"
x = re.findall(pat, text)

print(x)