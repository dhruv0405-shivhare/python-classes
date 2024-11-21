# positional arguement
'''
def add(x,y,z):
    z = x+y+z
    #print(z) 
    return z
p = int (input("enter 1st value"))
q = int (input("enter 2nd value"))
r = int (input("enter 3rd value"))

x = add(y=r,x=p,z=q)
print (x)

'''
'''
def add(*n):
	print(n)
	sum = 0
	for i in n:
	    sum = sum + i
	return sum
var = add(10,20,30,40,50,60)
print (var)
'''



def show(**kwargs):
	print (kwargs)
	for i,j in kwargs.items():
		print(i,"=",j)



show (name = 'dhruv' , age = 21 , quali = 'b.tech')


x = 10
def show():
	global y
	y = 20
	x = 50
	print(x)
	print(y)
	print(globals()['x'])
show()
print(x)
print(y)	




















