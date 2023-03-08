'''Write a Python program to write a list to a file.'''
def list_into_file(list, filename):
    file = open(f"{filename}", "w")
    file.writelines(list)
    file.close()

list = input().split()

filename = input()

list_into_file(list, filename)