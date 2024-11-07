# product.py

class Product:

    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def changeprice(self,newprice):
        self.price=newprice

#advantage is python is going to call it.
    def __str__(self):#this function will get called automatically when the need is
        #there to represent a product object in form of a string...
        return f"{self.name} - ${self.price:.2f}"
