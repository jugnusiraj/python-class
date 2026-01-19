# 1
# my_dict={
#     "name":"nik",
#     "age" :20
# }
# print(my_dict)
# output:{'name': 'nik', 'age': 20}

# 2
# my_dict={ "name":"nik","age" :20}
# print(my_dict["name"])
# output:nik

# 3
# my_dict={ "name":"nik","age" :20}
# my_dict["city"]="Delhi"
# print(my_dict)
# output:{'name': 'nik', 'age': 20, 'city': 'Delhi'}

# 4
# my_dict={ "name":"nik","age" :20}
# my_dict.update({"age":25})
# print(my_dict)
# output:{'name': 'nik', 'age': 25}

# 5
# my_dict={ "name":"nik","age" :20}
# del my_dict["age"]
# print(my_dict)
# output:{'name': 'nik'}

# 6
# my_dict={ "name":"nik","age" :20}
# print(my_dict.get("email"))
# output:None

# 7
# my_dict={ "name":"nik","age" :20}
# print(my_dict.keys())
# output:dict_keys(['name', 'age'])

# 8
# my_dict={ "name":"nik","age" :20}
# print(my_dict.values())
# output:dict_values(['nik', 20])

# 9
# my_dict={"a":1,"b":2}
# new=list(my_dict.items())
# print(new)
# output:[('a', 1), ('b', 2)]

# 10
# keys = ["name", "age"]
# values = ["Nik", 20]
# result=dict(zip(keys,values))
# print(result)
# output:{'name': 'Nik', 'age': 20}

# 11
# a={"a": 1, "b": 2, "c": 3}
# print(len(a))
# output:3

# 12
# x={"a":1}
# y={"b":2}
# x.update(y)
# print(x)
# output:{'a': 1, 'b': 2}

# 13
# my_dict={"x": 10, "y": 20}
# my_dict.clear()
# print(my_dict)
# output:{}

# 14
# my_dict={"a":10,"b":20}
# copy_dict=my_dict.copy()
# print(copy_dict)
# output:{'a': 10, 'b': 20}

# 15
# my_dict={ "name":"nik","age" :20}
# print(my_dict.get("salary"))
# output:None

# 16
# my_dict={"a": 1, "b": 2, "c": 3}
# last=my_dict.popitem()
# print(last)
# output:('c', 3)

# 17
# student = {"name": "Rahul", "marks": {"math": 90, "science":85}}
# print(student["marks"]["science"])
# output:85

# 18
# student = {"name": "Rahul", "marks": {"math": 90, "science":85}}
# student["marks"]["math"]=95
# print(student)
# output:{'name': 'Rahul', 'marks': {'math': 95, 'science': 85}}

# 19
# student = {"name": "Rahul", "marks": {"math": 90, "science":85}}
# student["marks"]["english"]=88
# print(student)
# output:{'name': 'Rahul', 'marks': {'math': 90, 'science': 85, 'english': 88}}

# 20
# student = {"name": "Rahul", "marks": {"math": 90, "science":85,'english': 88}}
# del student["marks"]["science"]
# print(student)
# output:{'name': 'Rahul', 'marks': {'math': 90, 'english': 88}}