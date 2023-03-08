'''Write a Python program to count the 
number of lines in a text file.'''
txtfile = input("write the text file(without ext. 'txt'):")

file = open(f"{txtfile}.txt", "r")

print(f"Number of lines in '{txtfile}.txt':",len(file.readlines()))

file.close()