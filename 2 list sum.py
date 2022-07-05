
d={"a":[3,6,2,5],"b":[3,1,1,8]}
for j in d:
    x=d[j]
    i=0
    sum=0
    while i<len(x):
        sum+=x[i]
        i+=1
    d[j]=sum
    print(sum)
print(d)

# dic={1,2,3,4,5}
# for j in dic:
#     x=dic[j]
#     i=0
#     sum=0
#     while i<len(x):
#         sum+=x[i]
#         i+=1
#     dic[j]=sum
#     print(sum)
# print(dic)
    
# a=["432"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c=int(a[i][j])*int(a[i][j])
#         print(c)
#         j=j+1
    # i=i+1



# a=["432"]
# i=0
# j=0

# while j<len(a[i]):
#     print(int(a[i][j])*int(a[i][j]))
#     j=j+1
    

# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c=int(a[i][j])*int(a[i][j])
#         print(c)
#         j=j+1
#     i=i+1






# a=[4,3,2]
# i=0
# while i<len(a):
#     c=a[i]**2
#     print(c)
#     i=i+1


l=[4,2,8,7,10,9,6]
i=0
l1=len(l)
while i<l1:
    x=l1//2
    if l1%2==0:
        print(l[x-1],l[x])
        break
    else:
        print(l[x])
        break
    i+=1
        
        