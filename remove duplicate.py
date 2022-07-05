

dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}

my_dic={}
# dup={}
for i in dic:
    if i not in my_dic:
        my_dic[i]=dic[i]
print(my_dic)





