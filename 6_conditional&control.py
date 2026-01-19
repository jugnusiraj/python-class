# a=input("enter a number")
# b=input("enter a number")
# print(a+b)

# a=int(input("enter a number"))
# if a>0:
#     print("positive number")

# elif a==0:
#     print("zero")
# elif a==-1:
#     print("-1")

# else:
#     print("negative numbers")
  


# Conditional and Control Statements in Python 
'''Control flow and conditional statements allow the execution of 
different blocks of code based on certain conditions. Python provides 
several ways to control the flow of your program using if-else 
statements, for and while loops, and other constructs. Let's dive into 
each of these with detailed explanations and examples.'''

# 1. Conditional Statements (if, elif, else) 
'''Python uses conditional statements to execute a block of code based 
on whether a condition evaluates to True or False. The basic form of 
conditional statements includes:'''

# a) if Statement 
'''The if statement evaluates a condition (a Boolean expression) and executes a block of code only if the
condition is True.'''

# Syntax: 
# if condition: 
'''code to execute if the condition is True'''

# a=int(input("enter a number"))
# if a>0:
#     print("positive number"-1)


# x=10
# if x>5:
#  print("x is greater than 5")

#  Output: x is greater than 5

# b) if-else Statement 
''' The else clause allows you to define what happens if the if condition is False.'''

# Syntax: 
# if condition: 
'''code to execute if the condition is True '''
# else: 
'''code to execute if the condition is False '''

# x=3
# if x>5:
#  print("x is greater than 5")

# else:
#  print("x is greater than or equal to 5")

# output:x is greater than or equal to 5



# c)if-elif-else Statement
'''The elif (short for "else if") allows you to check multiple conditions sequentially. If one condition is
True, the corresponding block is executed, and the rest of the conditions are skipped.'''

# Syntax: 
# if condition1: 
'''code to execute if condition1 is True '''
# elif condition2: 
'''code to execute if condition2 is True''' 
# else: 
'''code to execute if all conditions are False'''

# x = 7 
# if x > 10: 
#  print("x is greater than 10") 
# elif x > 5: 
#  print("x is greater than 5 but less than or equal to 10") 
# else: 
#  print("x is less than or equal to 5") 

# Output:x is greater than 5 but less than or equal to 10

# 2. Nested if Statements 
'''You can place if statements inside other if statements to create complex conditions. 
This is known as nesting.'''

# x = 10 
# y = 5 
# if x > 5: 
#  if y < 10: 
#   print("x is greater than 5 and y is less than 10") 

# output:x is greater than 5 and y is less than 10


# x = 10 
# y = 5 
# if x > 5:   (ee if work cheyythalle ithinte ullile if work aavukayollu)
#  if y < 10:  (if if work cheyythilekil ithinte ulilu ille else aahnu work aavuka)
#   print("x is greater than 5 and y is less than 10") 
#  else:
#   print("x is greater than 5 and y is not less than 10")
# else: (first le if work cheyythilekil ee else aahnu work aavuka)
#  print("x not greater than 10")  

# output:x is greater than 5 and y is less than 10

# 3. Python's if with and, or, not (Logical Operators)

'''a) and: Executes a block if both conditions are true. '''

# x = 10 
# y = 5 
# if x > 5 and y < 10: 
#  print("Both conditions are True")

#  Output: Both conditions are True 

'''b) or: Executes a block if any one of the conditions is true.''' 

# x = 10 
# y = 5
# if x > 5 or y > 10: 
#  print("At least one condition is True")

#  Output:At least one condition is True

'''c) not: Inverts the truth value of a condition.'''

# x = 10 
# y = 5
# if not x < 5: 
#  print("x is not less than 5")
 
 #  Output:x is not less than 5

# 4. Conditional Expressions (Ternary Operator)
'''Python allows for writing short, one-line if-else statements using the ternary operator. 
It can be useful for simple conditions.'''

# Syntax: 
'''expression_if_true if condition else expression_if_false'''

# x = 5 
# result = "Greater than 10" if x > 10 else "10 or less" 
# print(result)

# output:10 or less

# a=10
# operator='/'
# b=20
# if operator=='+':
#     print(a+b)
# elif operator=='-':
    # print(a-b)
# elif operator=='/':
#     print(a/b) 
# elif operator=='*':
#     print(a*b)   
# else:
#     print("invalid")    
   
'''ee situationil(division cheyyumbol 0 varuna situation)nested or ternery operation use aakaam'''
# a=10
# operator='/'
# b=0      
# if operator=='/':
#   if b==0:
#    print("denometer cannot be zero")
# else:
#  print(a/b)


# 5. Control Flow Statements
'''Control flow statements manage the flow of execution in loops and other constructs.'''

# a) The pass Statement 
'''The pass statement is used as a placeholder for future code. It allows you to write empty blocks that 
won't cause an error during execution.'''

# x = 5 
# if x > 3:
#     pass

# baki phone

# b)The continue Statement
'''The continue statement is used to skip the current iteration of a loop and move to the next iteration.'''

# for i in range(5): 
# if i == 3: # Skip the rest of the code for i == 3 

# continue  

# Skip the rest of the code for i == 3 

# Output: 
# 0 
# 1 
# 2 
# 4


# c)The break Statement
'''The break statement is used to exit a loop prematurely, regardless of whether the loop has finished
 all iterations.'''

# for i in range(5): 
# if i == 3: 
# break  # Exit the loop when i == 3 
# print(i) 
# Output: 
# 0 
# 1 
# 2

# 6. Loops in Python
'''Python supports two types of loops: for loops and while loops.'''

# a) for Loop
'''A for loop is used to iterate over a sequence (list, tuple, string, 
dictionary) or other iterable objects.'''

# Iterating over a list 

# fruits = ["apple", "banana", "cherry"] 
# for fruit in fruits: 
# print(fruit) 
# Output: 
# apple 
# banana 
# cherry

# b)while Loop
'''The while loop keeps executing a block of code as long as the specified condition remains True.'''

# x = 0 
# while x < 5: 
# print(x) 
# x += 1 
# Output: 
# 0 
# 1 
# 2 
# 3 
# 4 

# 7. else with Loops 
'''Python allows the use of an else statement with both for and while loops. The else block is executed 
when the loop completes all iterations without being interrupted by a break statement.'''

# Example with for loop: 

# for i in range(5): 
# print(i) 
# else: 
# print("Loop completed") 
# Output: 
# 0 
# 1 
# 2 
# 3 
# 4
# Loop completed

# Example with while loop: 

# x = 0 
# while x < 5: 
# print(x) 
# x += 1 
# else: 
# print("Loop completed") 
# Output: 
# 0 
# 1 
# 2 
# 3 
# 4 
# Loop completed

# 8. Nested Loops 
'''You can use loops inside loops, known as nested loops.'''

# for i in range(3): 
# for j in range(2): 
# print(f"i = {i}, j = {j}") 
# Output: 
# i = 0, j = 0 
# i = 0, j = 1 
# i = 1, j = 0 
# i = 1, j = 1 
# i = 2, j = 0 
# i = 2, j = 1

# 9. Infinite Loops 
'''An infinite loop occurs when the condition for a loop never becomes False. These loops can cause 
your program to run forever unless interrupted manually. '''

# while True: 
# print("This is an infinite loop")





# for loopil rangr print cheyyunath (me)

# for i in range(1,11):
#     print(i)
# output:1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for i in range(1,11,2):
#     print(i)
# output:1
# 3
# 5
# 7
# 9

# for i in range(2,11,2):
#     print(i)
# output:2
# 4
# 6
# 8
# 10


# a=10
# if a >10:
#     print('a is greater than 10')

# else:
#    print('a is not negative number')

# control flow statements:pass,break,continue
# code nte flow manage cheyyunath.

# pass
# if a >10:
#     pass  
# ivide oru condtion illa pakshe baakii conditions nu thadasam varaahn padilla ath kond aaahnu pass kodukunath.
# if nte avide endhekilum koduthal maatram work aavukayollu ninavil condition illa pakshe baaki illevareyum 
# break aakaruth iothaaghnu ivide udheshikunath.baaki illore error adikaahthe irikaahn

# else:
#    print('a is not negative number')
# output:a is not negative number

# break
# oru code avide vech stop cheyyanam pinnea load aavaruth athinaahnu break

# for i in range(1,11):
#     if i ==5:
#         break
#     print(i)
# output:1
# 2
# 3
# 4

    #  continue
# current iteration skip cheyyth baakiyullath continue cheyyanam ithaahnu continue kond udheshikunath

# for i in range(1,11):
#     if i ==5:
#         continue
#     print(i)
# output:1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# loops  forloop , while loop
# forloop

# a={'apple','bannana','cherry'}
# for i in a:
#   print(i)
# output:cherry   (ooro element aayii iduth tharumm)
# bannana
# apple

# whileloop  : condition etrekaalam true aahno athrim ah print aavumm.
# while condition false aavunath vere print aavum

# x=0
# while x<10:
#     print(x)
    # x+=1 
    # (ith endhayallum kodukanam current ivide ne varanam.indentation must aahnu        currect print nte adiyil thanea kodukanam)
# endlessly run cheyyth kondirikumm


# for i in range(5):
#     print(i)
# else:
#     print('loopfinished')
# output:0
# 1
# 2
# 3
# 4
# loopfinished

    # ivide for loop kazhinjal else work cheyyum
    #range ne aahnu ee i,polulla lletters soochipikunath endh venamegilum kodukaahm.


# nested loop

# for i in range(3):
#     for j in range(2):
#         print(f"i={i},j={j}")

'''oru loop koduthitt athinte ullile loop work cheyyum.ullile loop ethre pravshyam koduth athre pravshyam work aavum.(oru loopinte akath vere loop)'''
# output:i=0,j=0
# i=0,j=1
# i=1,j=0
# i=1,j=1
# i=2,j=0
# i=2,j=1


# list creat aakunath 

# a=[]
# for i in range (10):
#     a.append(i)
# print(a)
    # append nu paranjal avasanathek poyii kidakumm
# output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range (10):
#     print(i)
