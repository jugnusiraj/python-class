# setil slicing pattilla,presence check cheyyam
'''Python Sets:
A set in Python is a collection of unique and unordered elements. 
Unlike lists or tuples, sets do not allow duplicate values and are not 
indexed, meaning elements cannot be accessed via indexing. Sets are 
mutable, allowing modification, but the elements within the set must 
be immutable (e.g., numbers, strings, and tuples can be elements, but 
lists and dictionaries cannot). '''



# 1. Creating a Set 
'''Sets are created using curly braces {} or by calling the set() function.'''

#  Using curly braces
# a={1,2,3,4,5}
# print(a)
# print(type(a))
#  Output: {1, 2, 3, 4,5}

# a={"apple","orange","cherry","bananna"} 
# print(a)
# print(type(a))
#  Output:{'bananna', 'cherry', 'orange', 'apple'}
# <class 'set'>


# Using set() function 
# set = set([5, 6, 7]) 
# print(set)
# output:{5, 6, 7}

# Empty Set: To create an empty set, use the set() function, as {}  will create an empty dictionary.
# set = set() 
# print(set)
# output:set()


# 2. Accessing Set Items
'''Since sets are unordered, you cannot access items using indexing or 
slicing. You can, however, iterate through the items in a set using a 
for loop.'''
# Example: 
# my_set = {10, 20, 30, 40} 
# for item in my_set: 
# print(item) 
'''You can also check for the presence of an element in a set using the in keyword. '''
# my_set = {1, 2, 3} 
# print(2 in my_set)  # Output: True 
# print(5 in my_set)  # Output: False
    

# set = {1, 2, 3} 
# print(2 in set) 
#  # Output: True 
# print(5 in set)  
# # {1, 2, 3, 4, 5} False


# 3. Adding Items to a Set
'''You can add items to a set using the add() method or add multiple 
items using the update() method. '''

# a)Adding a Single Item:(single item add aakahn add use akunu)
# set={1,2,3,4}
# set.add(5)
# print(set)
# output:{1, 2, 3, 4, 5}

# b)Adding Multiple Items: (multiple item add akaahn update use aakunu)
# set={1,2,3,4}
# set.update([6,7,8,9])
# print(set)
# output:{1, 2, 3, 4, 6, 7, 8, 9}


# 4. Removing Items from a Set 
'''Sets provide several methods to remove elements: '''

# a)remove
''' Removes the specified element. If the element is not found, it raises a KeyError.'''
#eeth element ne remove cheyyaahn use cheyyunu eeth remove cheyyanam  ath kodukanam index wise 
# alla remove cheyyunath element aahnu idukunath ,remove cheyyuna element illekil error 
# kaaahnikum

# set={1,2,3,4,5,6}
# set.remove(2)
# print(set)
# output:{1, 3, 4, 5, 6}

# b)discard
''' Removes the specified element. If the element is not found, it does not raise an error.'''
#discard um remove cheyyaahn use cheyyunu ,remove cheyyune element illakil aa set thanea print aavum error kaahnikulla

# set={1,2,3,4,5,6}
# set.discard(3)
# print(set)
# output:{1, 2, 4, 5, 6}

# c)pop
'''Removes and returns a random item from the set since sets are unordered.'''
# set = {1, 2, 3, 4,5,6} 
# removed_item = set.pop() 
# print(removed_item)  
# Output: Random item (eg: 1)

#d)clear
'''Removes all items from the set.'''
# set = {1, 2, 3} 
# set.clear() 
# print(set) 
 # Output: set()

# 5. Joining Sets 
'''You can combine two or more sets using various methods: '''

#a) union
'''Returns a new set containing all items from both sets (duplicates removed). '''
# set1 = {1, 2, 3} 
# set2 = {3, 4, 5} 
# result =set1.union(set2) 
# print(result) 
 # Output: {1, 2, 3, 4, 5} 

# b) update
''' Updates the calling set with the union of itself and another set. '''
# set1 = {1, 2, 3} 
# set2 = {4, 5, 6} 
# set1.update(set2) 
# print(set1)  
# Output: {1, 2, 3, 4, 5, 6}

# c) Set Intersection (&)
'''Returns the common elements between two sets.'''
# set1 = {1, 2, 3} 
# set2 = {2, 3, 4} 
# result = set1 & set2 
# print(result)  
# Output: {2, 3}

# d)Set Difference (-)
''' Returns the items present in the first set but not in the second.'''
# set1 = {1, 2, 3} 
# set2 = {2, 3, 4} 
# result = set2 - set1
# print(result) 
 # Output: {4}

#e)Set Symmetric Difference (^) randillum pothuvayitt illathath
''' Returns items that are present in either set but not in both.'''
# set1 = {1, 2, 3} 
# set2 = {2, 3, 4} 
# result = set1 ^ set2 
# print(result)  
# Output: {1, 4}

# 6. Set Methods
'''Sets come with several built-in methods: 
 add(item): Adds a specified item to the set. 
 remove(item): Removes the specified item from the set (raises 
  an error if the item does not exist). 
 discard(item): Removes the specified item from the set (does 
  not raise an error if the item does not exist). 
 pop(): Removes a random item from the set and returns it. 
 clear(): Removes all items from the set, making it an empty set. 
 copy(): Returns a shallow copy of the set.'''

# Example: 
# set1 = {1, 2, 3} 
# set2 = set1.copy() 
# print(set2)  
# Output: {1, 2, 3}


''' union(set): Returns a new set containing all unique items from 
both sets. 
 update(set): Adds all items from another set to the current set. 
 intersection(set): Returns a set containing only the elements 
common to both sets. 
 difference(set): Returns a set containing elements only in the 
calling set and not in the other set. 
 symmetric_difference(set): Returns a set containing elements 
that are unique to both sets. 
 issubset(set): Returns True if all elements of the calling set are 
present in the other set.'''

# Example: 
# python 
# Copy code 
# set1 = {1, 2} 
# set2 = {1, 2, 3, 4} 
# print(set1.issubset(set2))  
# Output: True

#f) issubset(set): Returns True if all elements of the calling set are present in the other set. 

# set1 = {1, 2} 
# set2 = {1, 2, 3, 4} 
# print(set1.issubset(set2)) 
 # Output: True

#  issuperset(set): Returns True if all elements of the other set are 
# present in the calling set. 

#g)issuperset(set): Returns True if all elements of the other set are present in the calling set.
# set1 = {1, 2} 
# set2 = {1, 2, 3, 4} 
# print(set2.issuperset(set1)) 

# 7. Frozen Sets
'''A frozenset is an immutable version of a set. Once created, you 
cannot add or remove elements from a frozenset.'''
# my_frozenset = frozenset([1, 2, 3, 4]) 
# print(my_frozenset)  
# Output: frozenset({1, 2, 3, 4}) 

'''Frozensets are useful when you need a collection of unique elements 
that should not be modified.'''