'''Write a Python program with builtin function that checks 
whether a passed string is palindrome or not.'''
def isPol(str):
    return str == "".join(reversed(str))

str = input()

print(isPol(str))