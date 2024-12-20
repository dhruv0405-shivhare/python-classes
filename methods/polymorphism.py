# polymorphism --> same name function with different arugments.

# my_list = [10,20,'dhruv']
# my_string = "dhruv"

# print(len(my_string))
# print(len(my_list))

# Type  -->
#1. method overloading :
#2. method overriding  :


# error code
# class A :
#     def add (self,x,y):
#         return x+y
#     def add (self,x,y,z):
#         return x+y+z
# obj = A()
# obj.add(10,20)    


# class A :
#     def add (self,*n):
#         sum = 0
#         for i in n :
#             sum = sum + i
#         return sum
# obj = A()
# x=obj.add(10,20)
# print(x)  

# y=obj.add(10,20,30)
# print(y)  



#over riding -->

class c:
    def display (self):
        print("from class c")

class d(c):
    def  display(self):
         print("from class d")
    def p_display(self):
        self.display
        super().display()
obj = d()
obj.p_display()
obj.display()                   