




# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# print(student_marks)
# query_name = input()
# x=student_marks[query_name]
# print(x)
# def Average(x):
#     return sum(x) / len(x)

# average = Average(x)
# print("the average is =",(average) )



# if __name__ == '__main__':
#     N = int(input())
#     a = []
#     for i in range(N):
#         s = input().split()
#         if s[0] == "insert":
#             a.insert(int(s[1]),int(s[2]))
#         elif s[0]=="print":
#             print(a)    
#         elif s[0] == "remove":
#             a.remove(int(s[1]))
#         elif s[0] == "append":
#             a.append(int(s[1]))
#         elif s[0] == "sort":
#             a.sort()
#         elif s[0] == "pop":
#             a.pop()
#         elif s[0] == "reverse":
#             a.reverse()
        
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())  
#     print(a+b)
#     print(a-b)
#     print(a*b)
    
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0, n):
        # print(i ** 2)

# def is_leap(year):
#     leap = False
    
    # Write your logic here
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 leap=True
#             else:
#                 leap=False
#         else:
#              leap=True
#     else:
#         leap=False

#     return leap



# year = int(input())
# print(is_leap(year))


# from os import name


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n %2!=0:
#         print("weird")
#     if n>=2 and n<=5:
#         print("not weird")
#     if n>=6 and n<=20:
#         print("weird")
#     if n>20:
#         print("weird")
        

# if __name__ == '__main__':
#     n = int(input().strip())

#     if n% 2 != 0:
#         print ("Weird")
#     else:
#         if n >= 2 and N <= 5:
#             print ("Not Weird")
#         elif n >= 6 and N <= 20:
#             print ("Weird")
#         elif n > 20:
#             print ("Not Weird")
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end="")
                        