# dictionary -->
'''
1) it is a mapping data type in which each element is represented as key value pair .
2) it is a mutable data type
3) it is ordered data type --> element first inserted fetched first

note --> if we iterate a dictionary using for loop then data must be fatched in the order 
, in which it has been inserted.

4) representation of dictionary --> {}
5) esme indexing nhi hogi.
6) esme hum indexing pass nhi krte key pass krte h print krane ke lie.

'''

'''
d = {1:"monday" , 2:"tuesday" , 3:"wednesday"}
print(d)

print(d[2])
'''



# properties of key :
'''
1) key should be unique new key-value pair overwrite old key-value pair.
2) key must be consist of immutable data type.

d = {1:"monday" , 2:"tuesday" , 3:"wednesday" , 1:"jan" , 2:"feb" , 3:"march"}
print(d)

'''

#property of value :
'''
1) value can be duplicate.
2) calue can be consist of any data-type , 

d = {1:"monday" , 2:"monday" , 3:"monday"}
print(d)

'''

# dictionary me value add krni ho tb -->
d = {1:"monday" , 2:"tuesday" , 3:"wednesday"}
print(d)
d[4] = "thursday"
d[5] = "friday"
d[1] = "january"

d.update({6:"saturday"})
d1 = {7:"sunday"}
d.update(d1)
print(d)
