my_tuple = (70,75,60,85,25,40,80)

def greater_60(x):
    if x > 60 :
        return x
    
x =  (filter(greater_60,my_tuple))

print(list(x))