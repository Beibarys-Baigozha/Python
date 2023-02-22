'''Implement a generator that returns all 
numbers from (n) down to 0.'''
n = int(input())

myNumbers = (i for i in range(n, -1, -1))

print(type(myNumbers))

for x in myNumbers:
    print(x)