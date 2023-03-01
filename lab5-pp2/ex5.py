'''Write a Python program that matches a string 
that has an 'a' followed by anything, ending in 'b'.'''
import re

text = input()
pat = r"a.*b"
x = re.search(pat, text)

if x:
    print("yes")
else:
    print("no")