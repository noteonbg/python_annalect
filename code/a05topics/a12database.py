"""
-- Create products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Create orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


# Create a function for INSERT operation into products
def insert_product(product_name, category, price):
    cursor.execute(
        "INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s) RETURNING product_id",
        (product_name, category, price)
    )
    product_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Inserted product with ID: {product_id}")
    return product_id

# Create a function for INSERT operation into orders
def insert_order(product_id, quantity):
    cursor.execute(
        "INSERT INTO orders (product_id, quantity) VALUES (%s, %s) RETURNING order_id",
        (product_id, quantity)
    )
    order_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Inserted order with ID: {order_id}")
    return order_id

# Create a function for UPDATE operation (update product price based on product_id)
def update_product_price(product_id, new_price):
    cursor.execute(
        "UPDATE products SET price = %s WHERE product_id = %s",
        (new_price, product_id)
    )
    conn.commit()
    print(f"Updated price for product ID: {product_id}")

# Create a function for SELECT operation based on primary key (product_id)
def select_product_by_id(product_id):
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    print("Product details:", product)

# Create a function for SELECT operation based on non-primary key (product_name)
def select_product_by_name(product_name):
    cursor.execute("SELECT * FROM products WHERE product_name = %s", (product_name,))
    products = cursor.fetchall()
    print(f"Products with name {product_name}:")
    for product in products:
        print(product)

# Example Usage
if __name__ == "__main__":
    # Insert a new product
    product_id = insert_product("Widget A", "Electronics", 25.50)

    # Insert an order for the product
    insert_order(product_id, 100)

    # Update product price
    update_product_price(product_id, 27.00)

    # Select product by primary key (product_id)
    select_product_by_id(product_id)

    # Select product by non-primary key (product_name)
    select_product_by_name("Widget A")

    # Close the database connection
    cursor.close()
    conn.close()




\? list all the commands
\l list databases
\conninfo display information about current connection
\c [DBNAME] connect to new database, e.g., \c template1
\dt list tables of the public schema
\dt <schema-name>.* list tables of certain schema, e.g., \dt public.*
\dt *.* list tables of all schemas
Then you can run SQL statements, e.g., SELECT * FROM my_table;(Note: a statement must be terminated with semicolon ;)
\q quit psql


"""