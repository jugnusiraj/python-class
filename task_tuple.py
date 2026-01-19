# 1
# a=(1,2,3,4)
# print(a[2])
# output:3

# 2
# a=(10,20,30)
# b=list(a)
# print(b)
# output:[10, 20, 30]

# 3
# a=[1,2,3]
# b=tuple(a)
# print(b)
# output:(1, 2, 3)

# 4
# a=("a","b","c","d") 
# print(a[1:3])
# output:('b', 'c')

# 5
# a= ("x","y","z") 
# print("x" in a)
# output:True

# 6
# a=(5,3,9,1)
# print(max(a))
# output:9

# 7
# a=(1,2,3)
# print(a*2)
# output:(1, 2, 3, 1, 2, 3)

# 8
# a=(1,2,2,3,2)
# print(a.count(2))
# output:3

# 9
# a=("dog","cat","mouse") 
# print(a.index("cat"))
# output:1

# 10
# a=(1,2,3,4,5)
# print(a[::-1])
# output:(5, 4, 3, 2, 1)

# 11
# a=(1,2)
# b=(3,4)
# joining_tuple=a+b
# print(joining_tuple)
# output:(1, 2, 3, 4)

# 12
# a="hello"
# print(tuple(a))
# output:('h', 'e', 'l', 'l', 'o')

# 13
# a=(1,2,3,4)
# result=list((a[0], a[-1]))
# print(result)
# output:[1, 4]

# 14
# a=(10,20,30,40)
# b=list(a)
# b[2]=99
# print(b)
# a=tuple(b)
# print(a)
# output: [10, 20, 99, 40] ,(10, 20, 99, 40)

# 15
# a=(1,2,3)
# e,f,g=a
# print(e)
# print(f)
# print(g)
# output:1
       # 2
       # 3

# 16
# a=(1,2,3)
# nested=(a,)
# print(nested)
# output:((1, 2, 3),)

# 17
# a=['a','b']
# b=['c','d']
# result=tuple(a+b)
# print(result)
# output:('a', 'b', 'c', 'd')

# 18
# a=(1,2,3)
# print(a[::-1])
# output:(3, 2, 1)

# 19
# a = ([1, 2], [3, 4])

# flat_list = []
# for i in a:
#  flat_list.extend(i)
# print(flat_list)
# # output:[1, 2, 3, 4]

# 20
# a=(1, [2,3], 4) 
# a[1].append(5)
# print(a)
# output:(1, [2, 3, 5], 4)



