# Python Dictionaries
'''A dictionary in Python is an unordered collection of key-value pairs, 
where each key must be unique and immutable (like strings, numbers, 
or tuples), but the values can be of any data type. Dictionaries are 
mutable, meaning that you can add, remove, and modify items after 
they have been created.'''

# 1. Creating a Dictionary 
'''You can create a dictionary using curly braces {} or by calling the 
dict() constructor.'''

# a={
#     "name":"jugnu",
#     "age":"25",
#     "city":"palakkad"
# }
# print(a)
# output:{'name': 'jugnu', 'age': '25', 'city': 'palakkad'}


#a) Using curly braces 
# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# print(my_dict)
# output:{'name': 'abc', 'age': 30, 'city': 'malappuram'}

#b) Using the dict() constructor 
# another_dict=dict(name="minnu",age=25,city="kozhikod")
# print(another_dict)
# output:{'name': 'minnu', 'age': 25, 'city': 'kozhikod'}


#c)  Empty Dictionary: 
# a={}
# print(a)
#output:{}

# 2. Accessing Dictionary Items 
# my_dict={"name":"jugnu","Age":"25"}
# print(my_dict["name"])
# output:jugnu

# my_dict={"name":"jugnu","Age":"25"}
# print(my_dict["name1"])
# output:error varum because name1 variable avide illathath kond

# Using get():
# my_dict={"name":"jugnu","Age":"25"}
# print(my_dict.get("Age"))
# output:25

# my_dict={"name":"jugnu","Age":"25"}
# print(my_dict.get("city"))
#output:none because avide aa variable illathath kond ivide error kahnikulla(safe get use aakunath aahnu)

# 3. Changing Dictionary Items
'''You can modify a dictionary by assigning a new value to an existing key. '''

# my_dict={"name":"jugnu","Age":"25"}
# my_dict["Age"]=35
# print(my_dict)
# output:{'name': 'jugnu', 'Age': 35}

'''If the key doesn't exist, it will create a new key-value pair. '''

# my_dict={"name":"jugnu","Age":"25"}
# my_dict["city"]="kottayam"
# print(my_dict)
# output:{'name': 'jugnu', 'Age': '25', 'city': 'kottayam'}

# 4. Adding Items to a Dictionary 
'''You can add new key-value pairs to a dictionary by assigning a value to a new key. '''

# my_dict={"name":"jugnu","Age":"25"}

# my_dict={"name":"jugnu","Age":"25"}
# my_dict["city"]="kottayam"
# print(my_dict)
# output:{'name': 'jugnu', 'Age': '25', 'city': 'kottayam'}

# 5. Removing Items from a Dictionary
'''Dictionaries provide several ways to remove elements: '''

#a) pop(key):
''' Removes the element with the specified key and returns the value. If the key doesn’t exist, 
it raises a KeyError. '''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# age=my_dict.pop("age")
# print(my_dict)
# print(age)
# output:{'name': 'abc', 'city': 'malappuram'}

# b) popitem()
''' Removes and returns the last inserted key-value pair'''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# last_item=my_dict.popitem()
# print(last_item)
# output:('city', 'malappuram')

# c) del statement:
''' Deletes the specified key-value pair. '''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# del my_dict["city"]
# print(my_dict)
# output:{'name': 'abc', 'age': 30}

# d) clear(): 
''' Removes all elements from the dictionary.'''
# my_dict.clear() 
# print(my_dict)  
# Output: {}

# 6. Copying a Dictionary
# a)  Using copy()
''': Creates a shallow copy of the dictionary.'''

# orginal={'name': 'abc', 'age': 30}
# copy_dict=orginal.copy()
# print(copy_dict)
# Output:{'name': 'abc', 'age': 30}

# b) Using dict() constructor
# orginal={'name': 'abc', 'age': 30}
# copy_dict=dict(orginal)
# print(copy_dict)
# Output:{'name': 'abc', 'age': 30}

# 7. Nested Dictionaries 
'''Dictionaries can contain other dictionaries, allowing you to create complex data structures. '''

# nested_dict={ 
#     "person1":{'name': 'aaa', 'age': 30},
#     "person2":{'name': 'bbb', 'age': 35},
#     "person3":{'name': 'ccc', 'age': 25}
# }
# print(nested_dict["person1"],["name"])
# output:{'name': 'aaa', 'age': 30} ['name']
# print(nested_dict)
# output:{'person1': {'name': 'aaa', 'age': 30}, 'person2': {'name': 'bbb', 'age': 35}, 'person3': {'name': 'ccc', 'age': 25}}

'''You can access, modify,and add elements within nested dictionaries as you would with a normal dictionary'''

# nested_dict["person1"]["name"]="eee"
# print(nested_dict["person1"]["name"])
# # output:eee
# print(nested_dict)
# output:{'person1': {'name': 'eee', 'age': 30}, 'person2': {'name': 'bbb', 'age': 35}, 'person3': {'name': 'ccc', 'age': 25}}

# 8. Dictionary Methods 
'''Here are some commonly used dictionary methods:'''

#a)  keys(): 
'''Returns a view object that displays a list of all the keys in the dictionary.'''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# print(my_dict.keys())
# output:dict_keys(['name', 'age', 'city'])

# b) values()
'''Returns a view object that displays a list of all the values in the dictionary.'''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# print(my_dict.values())
# # output:dict_values(['abc', 30, 'malappuram'])

# c) update():
'''Updates the dictionary with the key-value pairs from another dictionary. '''

# my_dict = {"name": "abc", "age": 30, "city": "malappuram"}
# my_dict.update({"age":25,"city":"palakkad"})
# print(my_dict)
# output:{'name': 'abc', 'age': 25, 'city': 'palakkad'}

# d) fromkeys()
''' Creates a new dictionary from the given sequence of keys with the specified value. '''

# dict_keys = ["name", "age", "city"]
# new_dict=dict.fromkeys(dict_keys,"unknown")
# print(new_dict)
# output:{'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# e)setdefault(key, value):
'''Returns the value of the specified key.If the key doesn’t exist,it inserts the key withthespecifiedvalue'''

# my_dict = {"name": "John", "age": 30} 
# city = my_dict.setdefault("city", "New York") 
# print(city)      
# Output: New York 
# print(my_dict) 
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}  