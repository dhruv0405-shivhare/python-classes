# Zip() function --> zip is used for pairing key and value.

'''
key = ["dhruv" , "harsh" , "kartikey"]
value = [21 , 25 , 24 , 15 ,56]

result = dict(zip(key , value))
print(result)

result = tuple(zip(key , value))
print(result)

result = list(zip(key , value))
print(result)

'''

# Get(key) function --> return value
'''
data = {'dhruv':21 , 'kartikey':24 , 'harsh':24}
#  a = data['dhruv]
a = data.get('dhruv') # if we don't won't error than use .get function it will give (none) doesn't through error.
print(a)

'''

# setdefault() function 
# 1) Key available --> return existing value
# 2) Key not available --> key-value pair add , return added value 

'''
data = {'1':2390 , '2':2387 , '3':4533}

value = data.setdefault('1',999)

print(data)
print(value)


value = data.setdefault('11',999)

print(data)
print(value)

'''

#pop() , popitem() --> return delet value.

data = {'1':2390 , '2':2387 , '3':4533}
print(data)

value = data.pop('2')
print(data)
print(value)