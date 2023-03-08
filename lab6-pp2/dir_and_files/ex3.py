'''Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and 
directory portion of the given path.'''
import os

inp = input()

if os.path.exists(inp):
    filename = os.path.basename(inp)
    dirname = os.path.dirname(inp)
    print(f"Filename of the path :",filename )
    print(f"directory portion of the given path ':", dirname)
    
else:
    print("path does not exists")