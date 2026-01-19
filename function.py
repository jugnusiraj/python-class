# def greet(name):
#     print(f"hello {name}")

# greet("jugnu")
# greet("bbbb")


# def greet(a,b):
#     return a+b
# print(greet(10,30) )


# 1. Docstrings in Functions 
# def add(a,b):
#     """this function add two numbers"""
#     return a+b
# print(add.__doc__)
# print(add(10,40))
# Output: 
# This function adds two numbers.
# 50

# 2. Lambda Functions in Python 
# add=lambda a,b: a+b
# print(add(30,50))
# Output:80

# positional
# def greet (name,msg):
#     print(f"{name}{msg}")
# greet("aaa","how are yoy")

# default
# def greet(name, msg="Good morning"): 
#  print(f"{msg}, {name}!") 
# greet("aaa")


# keyword
# def greet(name, msg="Good morning"): 
#  print(f"{msg}, {name}!") 
# greet("bbb", "Good evening")