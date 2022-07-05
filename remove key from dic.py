# Q15.Write a Python program to remove a key from a dictionary.


d={"a":4,"b":5,"c":8,"e":2}
key=input("enter the key:")
if key in d:
    del d[key]
else:
    print("key not found")
print(d)