#lis1 = ['dhruv' , 'kartik' , 'harsh']

# lis1.reverse()
# print(lis1)

#inplace fuction are sort and reverse !!!



# these are 4 deleting function -->
#pop()
#remove()
#clear()
#del statement()


#pop() 

#pop() --> delete last element --> return deleted element
# pop() --> default last value delete krta h . in this we can pass index number.

# lis1 = ['dhruv' , 'kartik' , 'harsh', 'bhopal']
# print(lis1)
# deleted_value = lis1.pop(1)
# print(lis1)
# print(deleted_value)



#non return -->
#1.append()
#2.extend()
#3.sort()
#4.reverse()
#5.remove

# return -->
#1.index()
#2.len()
#3.max()
#4.min()
#5.sum()
#6.pop()




#remove() --->In this we can't use index number we have write name that we want to delete.. , in this we have to pass element

# lis1 = ['dhruv' , 'kartik' , 'harsh','harsh' , 'harsh' , 'bhopal']
# print(lis1)
# c = lis1.count('harsh')
# print(c)
# deleted_value = lis1.remove('harsh')
# deleted_value = lis1.remove('harsh')
# print(lis1)
# print(deleted_value)



#clear()---> this remove all the element'

# lis1 = ['dhruv' , 'kartik' , 'harsh','harsh' , 'harsh' , 'bhopal']
# print(lis1)
# lis1.clear()
# deleted_value = lis1.clear()
# print(lis1)
# print(deleted_value)



# del statement() -->

# lis1 = ['dhruv' , 'kartik' , 'harsh','harsh' , 'harsh' , 'bhopal']
# print(lis1)
# del lis1
# print(lis1) 



#slice() --> 
#        0    1   2      3       4    5   6     7         8    9   10
# lis1 = [ 12 , 3 , 5 , 'dhruv' , 12 , 58 , 75 , 'kartik'  , 55 , 34 , 45]
#        -11 -10 -9     -8      -7   -6   -5   -4        -3   -2   -1
# print(lis1)
# list [start : end : jump]
#jump -->by default 1 is taken
#end --> excluded (just before end)
# a = lis1[3 : 8 : 1]
# print(a)
# b = lis1[3 : 8 : 1]
# print(b)

# Note --> Slicing is used to get slice (sub sequence) of a sequence data type. 
    
# lis1 = [ 12 , 3 , 5 , 'dhruv' , 12 , 58 , 75 , 'kartik'  , 55 , 34 , 45]
# print(lis1)
# a = lis1[3:7]
# print(a)
# a = lis1[3::2]
# print(a)
# a = lis1[3:7]+lis1[8:]
# print(a)


#reverse print krane ke lie 
#in this we have to take jump in minus and it is mandatory otherwish it will give blank result

# lis1 = [ 12 , 3 , 5 , 'dhruv' , 12 , 58 , 75 , 'kartik'  , 55 , 34 , 45]
# a = lis1[7:2:-1]
# print(a)
# a = lis1[-4:-9:-1]
# print(a)
# a = lis1[::-1]
# print(a)


# 1. "here to learn"
# 2. "slicing is very helpful"
#3. "a rtlr"


# string = "we are here to learn python. and slicing is very helpful"
# print(string[7:21])
# print(string[33:56])
# print(string[3:19:3])

# print(string[3:19:3])
# print(string[:21] + "cpp" + string[27:])


# lis = ["dhruv" , "harsh" , "kartikey" , 4 , 18 , 29 , 54, 648 , 4465 ]
# a = lis[1:7:2]
# print(a)

# b = lis[-1:-8:-1]
# print(b)

# string = "we are here to learn python. and slicing is very helpful"

# # rete
# c = string[4:17:4]
# print(c)




s = "apple banana"
a = s[0:5:2]
print(a)

b = s[6:]
print(b)

c = s[-1::-1]
print(c)

d = s[6:] + " " + s[:5]
print(d)