'''Create a generator that 
generates the squares of numbers up to some number N.'''
n = int(input())

myNumbers = [i**2 for i in range(n)]
print(myNumbers)