# Create a dictionary from 2 lists, where the elements of 
# 1st list are the keys and the elements of the 2nd list 
# are the corresponding values.
# Example :-
# Input :-
# Code Example

a=["one","two","three","four","five"]
c=[1,2,3,4,5,]
i=0
b={}
while i<len(a):
    b[a[i]]=c[i]
    i=i+1
print(b)
