# # methods  -->
# # 1. Instant method  --> using self

class A:
     def new(self):                  #declaration
         print("1st method")

     def new1(self):
         self.new()                  # calling
         print("2nd method")
obj = A ()
obj.new()          # calling
obj.new1()



# # 2. Class method  --> using cls , @classmethod  --> static variable ki value modified krne ke lie use krte h 

class Book:
     price=150
     def __init__ (self , author , pages):
         self.author=author
         self.pages=pages
     @classmethod
     def update_price (cls,price):
          cls.price=price
     def show_details (self):
         print(self.author)
         print(Book.price)
         print(self.pages)     


obj = Book('Dhruv',200)
obj.show_details()
obj.update_price(200)
obj.show_details






# 3. Static method






#property

# 1. inheritance --> Parent child relation
class Gf:
    def name (self,Gf_name):
        self.z=Gf_name
    # def Gf_properties (self,age):
    #     self.a=age
        
class P(Gf):
    def __init__(self,p_name):
        self.x=p_name
    def p_properties (self,home,bank):
        self.h=home
        self.b=bank
        print(self.h)
        print(self.b)

class c(P):
    def c_properties(self,quali):
        self.q=quali
        self.p_properties('bhopal','HDFC')
        print(self.q)
        print(self.x)
        self.name('Shivram')
        print(self.z)
        print(self.a)
obj = c('Dhruv')
# obj.p_properties('bhopal','HDFC')
obj.c_properties('B.tech') 
# obj.Gf_properties(18) 

    
# print(dir(c))
# print(dir(obj))
