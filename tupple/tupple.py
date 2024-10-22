
#Tuple
#0 it is a container which store multiple data object .
#1. it is a sequence data type .(ordered data type)
#2. it is immutable data type .
#3. i) representation () , ii) comman seperated
#4. it is faster than list .  
#5. single element representation .
#6. generally whenever data is fetched from database it is stored in the form of tuple or dictionary .

# there is two type of container --> i)list , ii)tuple
#list --> []
#tuple -->()


# fruit = ("apple",20,100)

# print(type(fruit))

#fruit[2] = 200
# tuple is immutable .
# print(id(fruit))
# print(id(fruit[0]),id(fruit[1]),id(fruit[2]))



# fruit = ("apple",20,100)

# fruit = ("apple",20,100) + ("banana",200)
# print(fruit)

# number = (12,99) + (78 , 90)

# number = number + (89 , 90)

# print(number)  #In this their is 5 tupple object 

# note -->

#             0                    1
#   lis = [["ajay" , "dhruv"] , (45,54)]
#             0         1         0  1
#  print(type(lis[1]))
#lis[1][0] = 99 --> error  tuple does not change if tuple is in list.

# t = (4,5,[45,35,12])
# t[2][1] = 555
# print(t)

# lis = [["ajay" , "dhruv"] , (45,[65,65])]
# lis[1][1][0] = 999
# print(lis)


# len() , max() , min() , sum() , index() , count() --> these functions will work as same as list .

# t = (2,6,3,2)
# a = t.count(2)
# print(a)

# sorted() --> return sorted list .


# t = (2,6,3,2)
# a = sorted(t)
# print(a)

# t = (23)
# print(type(t))

# t = (23,)
# print(type(t))


# t1 = ("abcd")
# print(type(t1))


# t1 = ("abcd",)  # without coma the type will be string
# print(type(t1))

# t2 = 1,2,3,4,5    # --> without perenthisis it will called only tuple.
# print(type(t2))


# empty tuple --> two empty tuple

# 1. t = ()

# 2. t1 = tuple()
#    print(t,t1)


# record = ("ajay" , 101 , 32 , 6266680206)
# print (record)
# record = list(record)
# record[3] = 6262227670
# print (record)
# record = tuple(record)
# print (record ) 