'''Write a Python program that matches a 
string that has an 'a' followed by two to three 'b'.'''
import re

text = input()
pat = r'ab{2,3}'
x = re.search(pat, text)

if x:
    print("Yes")
else:
    print("no")