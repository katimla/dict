dic={1:10,2:60,3:30,5:50,4:60,5:30}
a={}
for key,value in dic.items():
    if value not in a:
        a[value]=[key]
    else:
        a[value].append(key)
print(a)

        