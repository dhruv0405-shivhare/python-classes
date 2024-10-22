# 3 mutable --> list , set , dictionary


# string -->
#1. squence
#2. immutable

#function of string

# msg = "apple is good 4 health"

#capitalize --> return capitalized string
# a = msg.capitalize()
# print(a)
# print(msg.capitalize())

# upper () -->
# print(msg.upper())
# b = msg.upper()
# print(b)

# lower () -->
# print(msg.lower())
# c = msg.lower()
# print(c)

# msg = "a3534657" #--> ek character to dena hi pdega integer hoga to false dega .

# isupper() --> return boolean output
# a = msg.isupper()
# print(a)

#islower () -->
# b = msg.islower()
# print(b)


# msg = "AaaBbb"
# isalpha -->

# a = msg.isalpha()
# print(a)

# msg = "1234"
# a = msg.isdigit()
# print(a)



#replace(old_value , new_value) -->

'''
s = "we are here to learn c++ , it is high level lang. "
s1 = s.replace("c++" , "python")
print (s1)

s2 = s.replace('a','b')
print (s2)

s3 = s.replace('a','b',1)
print (s3)

s4 = s.replace(s , "new")
print (s3)

'''

#split() --> return list

'''

s = "we are here to learn c++ , it is high level lang. "

s1 = s.split()
print(s1)

s2 = s.split('a')
print(s2)

s3 = s.split("here" , 1)
print(s3)

'''

# join() -->return string

'''
lis = ["apple" , "banana" , "pineapple" , "orange"]
lis1 = ("www" , "sss")

s = "".join(lis)
print(s)

s = " ".join(lis)
print(s)

s = " ".join(lis) + " " + " ".join(lis1)
print(s)

'''

s = "its now or never"
# s1 = "sti.won.ro.reven"

s = s.split()
print(s)

a = s[0][::-1]
b = s[1][::-1]
c = s[2][::-1]
d = s[3][::-1]

s=[a,b,c,d]
print(s)


s = ".".join(s)
print(s)