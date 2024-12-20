#encapsulation --> multiple units ko combined krke wrap krke ek single units me convert krna.

class A:
    x=10
    def __init__(self,name):
        self.name="Dhruv"
    @classmethod
    def show(cls,age):
        cls.age = 22
    @staticmethod
    def display(school):
        print(school)        




# access specifiers -->
#1. public   --> (govt. place)   x=10
#2. protected  --> (covered campus)  _x=10  --> single underscore means protected
#3. private      --> (private house)     __x=10  --> double underscore means private



#2. protected -->

class A:
    _x=10    #protected variable
    def _show (self):      #protected method
        print ("from class A")
class B(A):
    pass
print(dir(B))
class C:
    pass
print(dir(C))        


#3. private -->

class A:
    __x=10    #private variable
    def __show (self):      #private method
        print ("from class A")
class B(A):
    pass
print(dir(B))
obj = B()
print(obj._A__x)
obj._A__show()