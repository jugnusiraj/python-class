# for loopil rangr print cheyyunath

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

# list Comprehensions
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
# a=[x for x in range(1,11)if x %2==0]
# print(a)
# a=[x for x in range(1,11)if x %2!=0]
# print(a)