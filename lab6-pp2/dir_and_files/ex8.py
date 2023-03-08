'''Write a Python program to delete file by specified path. 
Before deleting check for access and whether
a given path exists or not.'''
import os

def delFile(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"file '{os.path.basename(path)}' was deleted")
        else:
            print("you do not have access")
    else:
        print("path does not exists")
        
inp = input()
delFile(inp)