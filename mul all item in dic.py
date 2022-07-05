# Q14.Write a Python program to multiply all the items in a dictionary.

d={"a":4,"b":5,"c":8,"e":2}
def pro(d):
    mul=1
    for i in d.values():
        mul*=i
    return mul
print(pro(d))