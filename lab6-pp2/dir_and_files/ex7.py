'''Write a Python program to copy the contents 
of a file to another file'''
def copyFile(file1, file2):
    f1 = open(f"{file1}", "a")
    f2 = open(f"{file2}", "b")
    f2.write(f1.read())
    f1.close()
    f2.close()
    
file1 = input()
file2 = input()

copyFile(file1, file2)