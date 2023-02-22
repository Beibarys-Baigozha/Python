'''Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0   '''
def areaPrll(height, lenght):
    return height*lenght

h = int(input("Length of base: "))
l = int(input("Height of parallelogram: "))

print("Area of parallelogram: ",areaPrll(h, l))