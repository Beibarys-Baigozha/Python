'''Write a Python program with builtin function that returns 
True if all elements of the tuple are true.'''
def tplT(tpl):
    return all(tpl)

tpl = (1, 3, "hello", 0)

print(tplT(tpl))
