# methods  -->
# 1. Instant method  --> using self

class A:
    def new(self):                  #declaration
        print("1st method")

    def new1(self):
        self.new()                  # calling
        print("2nd method")
obj = A ()
# obj.new()          # calling
obj.new1()



# 2. Class method  --> using cls , @classmethod  --> static variable ki value modified krne ke lie use krte h 

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