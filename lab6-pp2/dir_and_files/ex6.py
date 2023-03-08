'''Write a Python program to generate 26 text files 
named A.txt, B.txt, and so on up to Z.txt'''
def fileGen():
    for i in range(26):
        filename = chr(65 + i)
        open(f"{filename}.txt", "x")
        
fileGen()