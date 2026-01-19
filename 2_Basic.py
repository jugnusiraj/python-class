# print("hello world")

# indendation
'''Python uses indentation (whitespace at the  beginning of lines) to define the structure of the
code. Unlike  many other programming languages, Python does not use braces {} to delimit code 
blocks. (pythonil structure venam \ order venam)'''

# comments
# """Comments: Use # for single-line comments and triple quotes (''' or """) for multi-line comments.
'''print("five is greater than two")'''

# Case Sensitivity:
'''Python is case-sensitive, meaning Var and var are treated as two different variables.'''
# Var=5
# var=10
# print(Var,var)
# OUTPUT:5,10

# Variables in Python
'''1. Variable names must start with a letter or an underscore (_). 
   2. Variable names cannot start with a number. 
   3. Variable names can only contain alpha-numeric characters (A-Z, 
      a-z, 0-9) and underscores. 
   4. Variable names are case-sensitive.'''
# my_var=10
# user_id=25
# age=23

# Data Types in Python 
'''Python has several built-in data types that can hold different types of values. 
Some common data types include:'''

# 1. Numeric Types 
'''a)int: Represents whole numbers. '''
# Example: 
# age = 25 
# int 

'''b)float: Represents decimal numbers. '''
# Example: 
# price = 19.99 
 # float 

'''c)complex: Represents complex numbers with real and imaginary parts.''' 
# Example: 
# z = 2 + 3j 
 # complex 

# 2. String Type 
'''a)str: Used to represent text, enclosed in either single or double quotes. '''
# Example: 
# greeting = "Hello, World!" 
 # String 

# String operations: 

'''b)Concatenation:''' 
# name = "Alice" 
# message = "Hello " + name 
# print(message)  
# Output: Hello Alice 

'''c)Slicing:'''
# s = "Python" 
# print(s[0:3]) 
 # Output: Pyt 

# 3. Boolean Type 
'''bool: Represents two values: True or False.'''
# Example: 
# is_active = True  
# is_admin = False
# Boolean
  
# 4. List Type 
'''list: Used to store multiple items in a single variable. Lists are ordered, mutable, 
and can contain different data types. '''
# Example: 
# fruits = ["apple", "banana", "cherry"] 
# print(fruits[1])  
# Output: banana 

'''Lists can be modified (mutability):'''
# fruits[0] = "orange" 
# print(fruits)  
# Output: ["orange", "banana", "cherry"] 

# 5. Tuple Type 
'''tuple: Similar to lists, but tuples are immutable (cannot be changed after creation).''' 
# Example: 
# coordinates = (10, 20) 
# print(coordinates[0])  
# Output: 10 

# 6. Dictionary Type 
'''dict: A collection of key-value pairs, used to store data values in key-value pairs.
 Keys must be unique. '''
# Example: 
# user = {"name": "Alice", "age": 25} 
# print(user["name"])  
# Output: Alice 

# 7. Set Type 
'''set: An unordered collection of unique elements.''' 
# Example: 
# colors = {"red", "green", "blue"} 
# print(colors) 
 # Output: {'red', 'blue', 'green'}


#  Examples of Variable Assignment and Operations 
# 1. Variable Assignment:
# x=10
# y=3.5
# name="jugnu"
# is_student=True


# 2.   Arithmetic Operations: 
# a = 5 
# b = 3 
# print(a + b)  
# # Output: 8 
# print(a * b) 
#  # Output: 15 

# 3.  String Concatenation: 
# first_name = "John" 
# last_name = "Doe" 
# full_name = first_name + " " + last_name 
# print(full_name)  
# # Output: John Doe 

# 4.   List Operations: 
# numbers = [1, 2, 3, 4] 
# numbers.append(5) 
# print(numbers)  
# Output: [1, 2, 3, 4, 5]