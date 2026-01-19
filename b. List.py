# 1. Creating a List 
'''A list in Python is a collection of items that are ordered, changeable, 
and allows duplicate elements. Lists are one of the most commonly 
used data structures due to their versatility.'''

# Creating a list 
'''A list is created by placing elements inside square brackets [], 
separated by commas. Lists can store different data types.'''

# list=[1,2,3,"apple","orange"]
# print(list)
# output:[1, 2, 3, 'apple', 'orange']

# 2. Accessing List Items 
'''List items are accessed using index numbers, starting from 0 for the 
first item. Negative indexing can also be used to access elements from 
the end of the list.'''

# list=["apple","bananna","orangr","plum",1,2,3]
# print(list[1])
# output:bananna
# print(list[-1])
# output:3


#  a)Range of Indexes
'''You can use a range of indexes to access 
multiple items (slicing).''' 

# list=[10,20,30,40,50,60,70,80,90,100]
# print(list[0:5])
# output:[10, 20, 30, 40, 50]


# 3. Changing List Items 
'''Lists are mutable, meaning you can change their content after 
creation by assigning new values to specific index positions.'''

# list = ['apple', 'banana', 'cherry',"plum"] 
# list[1] = 'blueberry' 
# print(list)  
# output: ['apple', 'blueberry', 'cherry', 'plum']

# a)Changing multiple items: ''' Replacing values at index 1 and 2 '''

# list = [1, 2, 3, 4, 5] 
# list[1:3] = ['a', 'b']
# print(list)  
# output:[1, 'a', 'b', 4, 5]


# 4. Adding Items to a List 
'''Python provides several ways to add elements to a list:'''

# a)append(): Adds an item to the end of the list.

# list=["apple","cherry","bananna","plum"]
# list.append("blueberry")
# print(list)
# output:['apple', 'cherry', 'bananna', 'plum', 'blueberry']


# b)insert(): Inserts an item at a specific index. 

# list=["apple","cherry","bananna","plum"]
# list.insert(2,"orange")
# print(list)
# output:['apple', 'cherry', 'orange', 'bananna', 'plum']

# c)extend: Adds elements from another list (or any iterable) to the current list. 

# list = ['apple', 'bananna'] 
# new_list = ['plum', 'orange']
# list.extend(new_list)
# print(list)
# output:['apple', 'bananna', 'plum', 'orange']

# 5. Removing Items from a List
'''There are several methods to remove elements from a list:'''

# a) remove(): Removes the first occurrence of a specified item.

# list=["apple","cherry","bananna","plum"]
# list.remove("bananna")
# print(list)
# output:['apple', 'cherry', 'plum']

# b)pop(): Removes an item at the specified index and returns it. If no index is specified, 
# it removes the last item.

# list=["apple","cherry","bananna","plum"]
# popped_item= list.pop(1)
# print(list)
# output:['apple', 'bananna', 'plum']

# c)del: Deletes an item at a specific index or deletes the entire list.

# list=["apple","cherry","bananna","plum"]
# del list[0]
# print(list)
# output:['cherry', 'bananna', 'plum']

#d) clear(): Empties the entire list. 

# list = ['apple', 'banana', 'cherry']
# list.clear()
# print(list)
# output:[]

# 7. List method 
'''Python provides several built-in methods to manipulate lists.'''

# a)count(): Returns the number of occurrences of a specific value. 

# list=[1,2,3,4,5,6,7,8,9,10,4,4]
# print(list.count(4))
# output:3


# b)index(): Returns the index of the first occurrence of a specific value

# my_list = ['apple', 'banana', 'cherry'] 
# print(my_list.index('banana'))
# output:1

# c)reverse(): Reverses the order of the list. 

# my_list = [1, 2, 3] 
# my_list.reverse() 
# print(my_list) 
# output:[3, 2, 1]

# sort(): Sorts the list in ascending order. 

# my_list = [3, 1, 2] 
# my_list.sort() 
# print(my_list)
# output:[1, 2, 3]

# copy(): Returns a shallow copy of the list. 

# original_list = [1, 2, 3] 
# copied_list = original_list.copy() 
# print(copied_list) 
# output:[1, 2, 3]

# 8. Sorting a List 

# numbers = [3, 5, 1, 4, 2] 
# numbers.sort()  
# print(numbers)  
# numbers.sort(reverse=True)  
# print(numbers)  
# output:[1, 2, 3, 4, 5]
#        [5, 4, 3, 2, 1]

# a)sorted(): Returns a new sorted list, leaving the original list unchanged.

# original = [3, 1, 4] 
# sorted_list = sorted(original) 
# print(sorted_list)
# output:[1, 3, 4]

# 9. Copying a List 
'''To copy a list, you can use the copy() method or list slicing'''

# original_list = ['apple', 'banana', 'cherry'] 
# Using copy() method 
# copied_list = original_list.copy() 
# print(copied_list)
# output:['apple', 'banana', 'cherry']

# Using slicing 
# copied_list = original_list[:] 

# 10. Joining Lists 
'''You can join two or more lists using the + operator or the extend() method.''' 

# a)Using +:
# list1 = ['apple', 'banana'] 
# list2 = ['cherry', 'orange'] 
# combined_list = list1 + list2 
# print(combined_list)
# output:['apple', 'banana', 'cherry', 'orange']

# b)Using extend(): 
# list1 = ['apple', 'banana'] 
# list2 = ['cherry', 'orange'] 
# list1.extend(list2) 
# print(list1)
# output:['apple', 'banana', 'cherry', 'orange']


# 11. List Comprehensions
'''List comprehensions provide a concise way to create lists based on existing lists or iterables.
 They offer a more readable and faster approach to generating lists.'''

# a=[]
# for i in range(10):
#         a.append(i)
# print(a)

# for i in range(10):
#  print(a)

# Syntax: 
# new_list = [expression for item in iterable if condition] 

# Create a list of squares from 1 to 5 
# squares = [x**2 for x in range(1, 6)] 
# print(squares)  # Output: [1, 4, 9, 16, 25] 

# Example with condition: 
# Create a list of even numbers from 1 to 10 
# even_numbers = [x for x in range(11) if x % 2 == 0] 
# print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]



# list creat aakunath 

# a=[]
# for i in range (10):
#     a.append(i)
# print(a)
    # append nu paranjal avasanathek poyii kidakumm
# output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range (10):
#     print(i)

# list Comprehensions (me)
# list create cheyyaahn ulla contious way.it powerfull

# a=[x for x in range(10)]
# print(a)
# output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a=[x**2 for x in range(10)]
# # print(a)
# # output:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# a=[x-3 for x in range(10)]
# print(a)
# # output:

# a=[x**2 for x in range(1,11)if x %2==0]
# print(a)
# a=[x**2 for x in range(1,11)if x %2!=0]
# print(a)
