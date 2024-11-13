class Product:
    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def getprice(self):
        return self.price

    
    def from_csv_row(cls,row):
        product_id, name, category, quantity, price = row
        """we created the object from the input got from the list"""
        return cls(int(product_id), name, category, int(quantity), float(price))
    
# Example CSV row
csv_row = ['101', 'Widget', 'Gadget', '25', '19.99']
#list contents belong to which data type.

# Create a Product object using the class method
product = Product.from_csv_row(csv_row)

# Print the created product object
print(f"Product ID: {product.product_id}")
print(f"Name: {product.name}")
print(f"Category: {product.category}")
print(f"Quantity: {product.quantity}")
print(f"Price: ${product.price:.2f}")
