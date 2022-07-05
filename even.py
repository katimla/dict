# a=[1,2,3,4,5,6]
# i=1
# even=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         even=a[i]
#         b.append(even)
#     i=i+1
# print(b)



d={"a":[3,6,2,5],"b":[3,1,1,8]}
for j in d:
    # x=d[j]
    i=0
    b=[]
    while i<len(d[j]):
        if d[j][i]%2==0:
            b.append(d[j][i])
        i=i+1
    d[j]=b
print(d)