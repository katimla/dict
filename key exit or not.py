# Write a program to print 'exists' if entered key already
# exists in the dictionary and print 'not exists' if the entered
# key does not exist.



key=input("enter key:")
dict1={"name":'raju',"age":21}
if key in dict1.values():
    print("exits")
else:
    print("not exits")



