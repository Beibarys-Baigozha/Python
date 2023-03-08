'''Write a Python program with builtin function that accepts a string 
and calculate the number of upper case letters and lower case letters'''
str = input()
lowCase = 0
upCase = 0

for i in str:
    if i.isupper():
        upCase += 1
    else:
        lowCase += 1

print("number of upper case letters is: ", upCase)
print("number of lower case letters is: ", lowCase)