# 1
# a=int(input("enter a number:"))
# if a>0:
#     print("positive number")
# elif a<0:
#     print("negative number")    
# else:
#     print("zero")    

# output:enter a number:20
        # positive number

# 2
# a=int(input("enter a number:"))
# if a %2==0:
#  print("print even number")
# else:
#  print("odd number")

# output:enter a number:25
        #  odd number

# 3
# a=int(input("enter a number:"))
# if a>100:
#     print("greaterthan 100")
# else:
#     print("not greaterthan 100") 
#    
# output:enter a number:200
        # greaterthan 100
        # enter a number:100
        # not greaterthan 100

# 4
# age=int(input("enter a age: "))
# if age >=18:
#     print( "eligibl for vote")
# else:
#     print("not eligible for vote")    

# output:enter a age: 21
        #  eligibl for vote

# 5
# a=int(input("enter a:" ))
# b=int(input("enter b:" ))
# if a >b :
#     print("a is greater number")
# else:
#     print("b is greater number")

# output:enter a:30
       # enter b:10
       # a is greater number: 30

# 6
# a=int(input("enter a:" ))
# b=int(input("enter b:" ))
# c=int(input("enter c:" ))
# if a>=b and a>=c:
#   print(a)
# elif b>=a and b>=c:
#   print(b)
# else:
#   print(c)  
# output:
# enter a:30
# enter b:20
# enter c:10
# largest num:30

# 7
# year=int(input("enter a year"))
# if year%4==0 and  year %100!=0 or year %400==0:
#   print("leap year")
# else:
#   ("not a leap year")

# 8
# marks=int(input("enter the marks: "))
# if marks >=40:
#     print("pass")
# else:
#     print("fail")    

# output:
# enter the marks:
  # pass

# 9
# marks=int(input("enter the marks: "))
# if marks<=90:
#     print("A")
# elif marks<=75:
#     print("B")
# elif marks<=60:
#     print("c")    
# else:
#     print("fail")

# output:
# enter the marks: 85
# A


# 10
# character=(input("enter a character:" ))
# if character in "aeiou":
#     print("vowels")
# else:
#     print("consonant")    

# output:
# enter a character:aeiou
# #    vowels

# 11
# for i in range (0,11):
#     if i ==6:
#         break
#     print(i)

# output:0
# 1
# 2
# 3
# 4
# 5

# 12
# for i in range(1,11):
#      if i ==5:
#         continue
#      print(i)
# output:0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# 13
# a=10
# if a >10:
#   pass 
# print("no error")

# output:no error
# pass statement is used as a placeholder for future code.
# it avoid error and keep the code running and it fill empty block.

# 14
# for i in range(1,20):
#     if i%2==0:
#         print(i)

# output:2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

# 15
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)
# output:55

# 16
# x = int(input("Enter number: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Multiple of 3 and 5")
# else:
#     print("Not a multiple")

# output:Enter number: 15
        # Multiple of 3 and 5

# 17
# for i in range(5):
#     print("hello")
# output:
# hello
# hello
# hello
# hello
# hello

# 18
# list=[1,2,3,4,5]
# for i in  list:
#  if i >3:
#     print(i)
# output:4,5

# 19

# correct_user="admin"
# password="1234"
# max_login_attempt=3

# 20

# LIST COMPREHENSION ANS
# 1
# x=[1,2,3,4,5,6,7,8,9]
# print("sum:", sum(x))
# print("Even sum:", sum([i for i in x if i % 2 == 0]))
# print("Odd sum:", sum([i for i in x if i % 2 != 0]))

# output:sum: 45
# Even sum: 20
# Odd sum: 25

# 2
# nums = [3, 6, 9, 12, 15, 18, 20, 25]

# result = [i for i in nums if i > 10 and i % 3 == 0]
# print(result)
# output:[12, 15, 18]

# 3
# numbers = [2, 5, 8, 10, 12, 14, 17, 20]

# result = [i for i in numbers if i > 10 and i % 2 == 0]
# print(result)
# output:[12, 14, 20]

# 4
# words = ["apple", "banana", "cat", "dog"]

# lengths = [len(words) for word in words]
# print(lengths)
# output:[5, 6, 3, 3]

# 5
# nums = [1, 2, 3, 4, 5]

# result = ["even" if n % 2 == 0 else "odd" for n in nums]
# print(result)
# output:['odd', 'even', 'odd', 'even', 'odd']