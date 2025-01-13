from functools import reduce

my_list = [5,4,2,6,5]

power_function = lambda x , y: x+y 

powered_function = reduce(power_function,my_list)

print(powered_function) 