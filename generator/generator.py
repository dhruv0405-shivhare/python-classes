
def even_no(n):
    i=2
    while i<=n:
        yield i
        i=i+2
n=int(input("enter number"))
data = even_no(n)
print(data)
data1 = even_no(n)   
print(next(data1))
# data3 = even_no(n)   
# print(next(data3))
print("hello")
print(next(data1))
print("welcome")
print(next(data1))
