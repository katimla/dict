# def average(d,i):
#     sum=0
#     for key in d:
#         sum+=d[key][i]
#     return sum/len(d[key])
# def all_mark(d):
#     i=0
#     while i<3:
#         x=average(d,i)
#         print(x)
#         i+=1
# d={"abi":[10,20,30],"biju":[60,23,45],"ruchi":[50,30,56]}
# all_mark(d)



def  max_m(d,i):
    max=0
    for key in d:
        a=key
        x=d[key][i]
        if x>max:
            max=x
            z=a
    return z
def max_no(d):
    i=0
    while i<3:
        y=max_m(d,i)
        print(y)
        i+=1
d={"abinash":[10,220,30],"biju":[160,123,145],"ruchi":[50,30,56]}
max_no(d)