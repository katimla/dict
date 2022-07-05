# take input of ary.name and marks of 10 students and 
# store to a diction



i=1
a=[]
b=[]
while i<=3:
    user=input("enter the user name:")
    user1=int(input("enter the mark of the student:"))
    a.append(user)
    b.append(user1)
    j=0
    c={}
    while j<len(a):
        c[a[j]]=b[j]
        j=j+1
    i=i+1
print(c)