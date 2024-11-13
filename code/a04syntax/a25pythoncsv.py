import csv

# Define a Product class representing a manufactured item
class Product:
    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.quantity}, {self.price})"

    # Convert object data to a CSV-friendly list (to write to CSV)
    def to_csv_row(self):
        return [self.product_id, self.name, self.category, self.quantity, self.price]

    # Class method to create a Product from a CSV row (to read from CSV)
    @classmethod
    def from_csv_row(cls, row):
        product_id, name, category, quantity, price = row
        return cls(int(product_id), name, category, int(quantity), float(price))
    





# Sample products
products = [
    Product(1, "Widget", "Gadget", 100, 19.99),
    Product(2, "Gizmo", "Gadget", 150, 29.99),
    Product(3, "GadgetPro", "Gadget", 50, 49.99),
    Product(4, "Sprocket", "Tool", 200, 15.49),
]









# Write products to a CSV file
def write_products_to_csv(products, filename='products.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file) #  we want the write function with respect to csv
        
        # Write the header row
        writer.writerow(['product_id', 'name', 'category', 'quantity', 'price'])
        
        # Write each product as a row in the CSV
        for scrap in products:
            writer.writerow(scrap.to_csv_row())  #writes the csv content you gave into the file


        
        print("written successfully")

#write_products_to_csv(products)


# Read products from a CSV file and return a list of Product objects
def read_products_from_csv(filename='products.csv'):
    products = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        # Read each row and create a Product object
        for row in reader:
            product = Product.from_csv_row(row)# this row contains list of values separated by ,
            products.append(product)
    
    return products

# Read products from the CSV file
read_products = read_products_from_csv()
for product in read_products:
    print(product)


"""
to_csv_row method: This method converts the Product object to a list format that can be written to a CSV file (matching the header columns).
from_csv_row class method: This method is used to convert a row from the CSV back into a Product object.
Writing CSV: We open a file in write mode ('w') and use the csv.writer object to write the headers and the Product data.
Reading CSV: We open the CSV file in read mode ('r') and use csv.reader to parse the rows. Each row is then converted back into a Product object using the from_csv_row method.

"""


