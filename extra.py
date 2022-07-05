i=0
n="my name is katim 1234"
a=n.split()
i=0
while i<len(a):
    if a[i].isnumeric():
        print(a[i])
    i+=1