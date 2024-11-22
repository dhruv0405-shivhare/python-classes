import functools.reduce

my_tuple = (10,20,30,40,50)

def max_digit(x,y):
    if x > y:
        return x
    else:
        return y
    
x = reduce(max_digit,my_tuple)    