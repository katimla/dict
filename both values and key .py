a=["one","two","three","four","five"]
i=0
e={}
b={}
while i<len(a):
    e[i+1]=a[i]
    i=i+1
print(e)
b["numbers"]=e
print(b)

# a=["one","two","three"]
# b=["lays","chips","laphoi"]
# c=["numbers","snacks"]
# d1={}
# d2={}
# x=[]
# i=0
# while i<len(a) and i<len(b):
#     d1[i+1]=a[i]
#     d2[i+1]=b[i]
#     i+=1
# x.append(d1)
# x.append(d2)
# j=0
# d3={}
# d4={}
# while j<len(c) and j<len(x):
#     d3[c[j]]=x[j]
#     j+=1
# d4["dict"]=d3
# print(d4)

