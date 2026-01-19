# string
'''A string in Python is a sequence of characters enclosed in either single (') or double (") 
quotes.'''
# string = "Hello, World!" 
# print(string)

# 1. String Slicing 
''' Slicing allows you to extract parts of a string using a specific range of indices.
(oru portion idukaahn.)'''
'''Syntax: string[start:end:step] 
o start: The starting index (inclusive). 
o end: The stopping index (exclusive). 
o step: The interval between characters (optional).'''


# a)Basic slicing:
# s="hello,world!"
# print(s[0:5])
# output:hello

# b)Negative indices: Negative numbers can be used to start slicing from the end.
# s="hello,world!"
# print(s[-6:-1])
# Output: World 

# c)Skipping characters(step)
# s="hello,world" 
# print(s[0:12:2])
# output:hlowrd


# d)Reversing a String
# s="hello,world!"
# print(s[::-1])
# output:!dlrow,olleh

# 2. Modifying Strings
'''Strings in Python are immutable, meaning they cannot be changed once created. However,
   you can create a new string by modifying the original. '''

# a)Replace Method:This method replaces part of the string with a new substring.
# s = "Hello, World!" 
# a = s.replace ("Hello","my")
# print(a)
# output:my, World!

# b)Uppercase and Lowercase Conversion:upper() and lower() can be used to change the case. 
# a="Hiii How are YOU"    
# print(a.upper())
# Output: HELLO, WORLD!
# print(a.lower())
# Output: hello, world! 


# 3. String Concatenation 
'''String concatenation refers to joining two or more strings into one. '''

# a) Using + operator
# s1 = "Hello" 
# s2 = "World" 
# result = s1 + "," + s2 + "!" 
# print(result) 
# output:Hello, World!


# b)Using join() method
# words="my","name","is","jugnu"
# sentence = " ".join(words) 
# print(sentence)
# output:my name is jugnu

# 4. Format Strings 
'''Python provides several ways to format strings, allowing you to inject 
values into a string template.'''

# a) Using % operator
'''Similar to printf in C, where %s is used for strings, %d for integers, etc. '''

# name = "JUGNU" 
# age = 25 
# formatted_string = "My name is %s, and I am %d years old." % (name, age) 
# print(formatted_string) 
# output:My name is JUGNU, and I am 25 years old. 

# b)Using format() method
'''The format() method allows positional and keyword formatting.'''

# name = "JUGNU" 
# age = 26
# formatted_string = "My name is {}, and I am {} years old.".format(name, age) 
# print(formatted_string)  
# Output: My name is jugnu, and I am 25 years old.


# Keyword arguments
# formatted_string = "My name is {n}, and I am {a} years # old.".format(n="JUGNU", a=26)
# print(formatted_string)
# Output: My name is JUGNU, and I am 26 years old.

 # c. Using f-strings (Python 3.6+)
'''The most modern and efficient way to format strings. '''

# name = "jugnu" 
# age = 27 
# formatted_string = f"My name is {name}, and I am {age} years old." 
# print(formatted_string)
# Output: My name is jugnu, and I am 27 years old.


# 5. Escape Characters 
# Common Escape Characters: 
# \n: Newline 
# \t: Tab 
# \ \': Single quote 
# \": Double quote 
# \: Backslash

# a)Inserting a newline 
# print("Hello\nWorld") 
# Output: 
# Hello 
# World

# b)Inserting a tab 
# print("Hello\tWorld") 
 # Output: Hello    World


# c) Using quotes within a string 
# print('He said, "Python is amazing!"') 
  # Output: He said, "Python is amazing!"


# 6. String Methods 

'''Python provides a rich set of string methods to manipulate strings.''' 

# a)len(): Returns the length of the string. 
# s = "Hello, World!" 
# print(len(s)) 
# Output: 13  

# b) strip(): Removes leading and trailing whitespace. 
# s = "  Hello, World! " 
# print(s.strip()) 
#output:Hello, World! 

# c)split(): Splits the string into a list of substrings based on a separator. 
# s = "Hello, World!" 
# print(s.split(","))
#output: ['Hello', ' World!']

# d)find(): Returns the index of the first occurrence of a substring. Returns -1 if the substring 
# is not found. 
# s = "Hello, World!" 
# print(s.find("World"))
# Output:7

# e) count(): Returns the number of times a substring occurs in the string. 
 # s = "Hello, Hello, World!" 
# print(s.count("Hello"))  
 # Output: 2

# f)startswith() and endswith(): Check if a string starts or ends with a specific substring. 
# s = "Hello, World!" 
# print(s.startswith("Hello")) 
# # Output: True  
# print(s.endswith("World!"))   
# Output: True 

# g)upper() and lower(): Convert the string to uppercase or lowercase. 

# s = "Hello, World!" 
# print(s.upper()) 
# Output: HELLO, WORLD! 
# print(s.lower()) 
# Output: hello, world! 

# h) replace(): Replaces a substring with another substring. 
# s = "Hello, World!" 
# print(s.replace("World", "Python!"))
 # Output: Hello, Python!