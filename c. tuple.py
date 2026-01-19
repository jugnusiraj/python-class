'''Python Tuples: 
A tuple in Python is an ordered, immutable collection of items. 
Tuples are similar to lists but are immutable, meaning their content 
cannot be changed after they are created. Tuples are typically used for 
data that should not be changed, such as configuration values or 
coordinates.'''

# 1. Creating a Tuple 
'''Tuples are created by placing items inside parentheses (), separated by 
commas. You can store multiple data types in a tuple.'''

# a=("apple","bananna","orange","plum")
# print(a)
# print(type(a))
# output:('apple', 'bananna', 'orange', 'plum')
# <class 'tuple'>

''' Single Item Tuple: To define a tuple with a single item, you 
need to include a comma after the item.'''
# a = (5,) 
# print(type(a))  
# Output: <class 'tuple'>

# 2. Accessing Tuple Items 
'''Tuple items are accessed using index numbers, starting from 0. Like 
lists, you can use positive or negative indexing to access elements. '''

#a) Slicing Tuples: You can access a range of items using slicing.
# a = (10, 20, 30, 40, 50) 
# print(a[1:4])    
# Output: (20, 30, 40)

# a=("apple","bananna","orange","plum")
# print(a[1])
# output:bananna
# print(a[-1])     
# Output: 'plum' (last item)

# a=("apple","bananna","orange","plum")
# a=(1,2,3,4,5,6)
# print(a)
# output:(1, 2, 3, 4, 5, 6)


# 3. Updating a Tuple
'''Tuples are immutable, meaning you cannot change their values after 
creation. However, there are workarounds to achieve similar results, 
such as reassigning the entire tuple or converting it to a list.'''

#a) Reassigning a Tuple:
# a=("apple","bananna","orange","plum")
# b=list(a)
# b[1]="cherry"
# a=tuple(b)
# print(a)
# output:('apple', 'cherry', 'orange', 'plum')

#b) Convert Tuple to List: Convert a tuple to a list, update the list, and convert 
# it back to a tuple. 
# a = ('apple', 'banana', 'cherry') 
# temp_list = list(a) 
# temp_list[1] = 'orange'  # Changing the second item 
# a = tuple(temp_list) 
# print(a)         
 # Output: ('apple', 'orange', 'cherry')



#4. Unpacking Tuples 
'''Unpacking refers to extracting the values of a tuple into individual 
variables. The number of variables should match the number of items 
in the tuple.'''

# a=("apple","bananna","orange","plum")
# (e,f,g,h)=a
# print(e)
# print(f)
# print(g)
# print(h)
# output:apple
# bananna
# orange
# plum


# Using * (asterisk): You can use an asterisk to unpack remaining  items into a list.

# asterisk:remain item thine use idukunath,star ittit 
# a=("apple","bananna","orange","plum","cherry")
# (*e,f,g)=a
# print(e)
# print(f)
# print(g)
# output:['apple', 'bananna', 'orange']
# plum
# cherry

#  5. Joining Tuples:using+
'''You can concatenate two or more tuples using the + operator. '''

# a=("apple","bananna","orange","plum","cherry")
# b=(1,2,3,4,5,6)
# joining_tuple = a+b
# print(joining_tuple)
# output:('apple', 'bananna', 'orange', 'plum', 'cherry', 1, 2, 3, 4, 5, 6)

# 6. Tuple Methods 
'''Since tuples are immutable, their methods are limited compared to 
lists. There are two main methods available for tuples:'''

# a)count():  Returns the number of times a specified value appears in the tuple. 
# a=(1,2,2,2,3,4,5,6,7,8,9,2,2)
# print(a.count(2))
# output:5

# b)index(): Returns the index of the first occurrence of the specified value. 
# a=("apple","bananna","orange","plum","cherry")
# print(a.index("plum"))
# output:3

# 7. Tuples vs Lists 
''' Mutability: Lists are mutable, whereas tuples are immutable. 
    Performance: Tuples are generally faster than lists because of 
    their immutability. 
    Use Cases: Tuples are used for fixed data, such as coordinates, 
    while lists are used for collections that need to change.'''

#8. Deleting a Tuple
'''Although tuples themselves are immutable, you can delete an entire 
tuple using the del keyword.'''
# a=("apple","bananna","orange","plum")
# del a
# print(a)
# output:name 'a' is not defined
