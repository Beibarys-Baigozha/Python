'''Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5   '''
def trapArea(h, a, b):
    S = h*(a + b)/2
    return S

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

S = trapArea(h, a, b)

print("Area: ", S)