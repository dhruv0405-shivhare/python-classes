my_list = [5,4,9,8,7,5,2,6,4,5,9]

filter_function = lambda x:x % 2 != 0

filter_list = list(filter(filter_function , my_list))

print(filter_list)