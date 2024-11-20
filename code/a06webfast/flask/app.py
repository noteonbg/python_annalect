from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Secret key for session management and flash messages
app.secret_key = 'your_secret_key'

# In-memory storage for products
products_db = {}

# Route to Home page: Display all products
@app.route('/')
def index():
    return render_template('index.html', products=products_db)

# Route to create a product (GET and POST)
@app.route('/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        if not name or not price:
            flash('Name and price are required', 'error')
            return redirect(url_for('create_product'))
        
        productid = len(products_db) + 1
        products_db[productid] = {'productid': productid, 'name': name, 'price': float(price)}
        
        flash(f'Product "{name}" added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create.html')

# Route to update a product (GET and POST)
@app.route('/edit/<int:productid>', methods=['GET', 'POST'])
def edit_product(productid):
    product = products_db.get(productid)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        if not name or not price:
            flash('Name and price are required', 'error')
            return redirect(url_for('edit_product', productid=productid))
        
        product['name'] = name
        product['price'] = float(price)
        
        flash(f'Product "{name}" updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', product=product)

# Route to delete a product
@app.route('/delete/<int:productid>')
def delete_product(productid):
    product = products_db.pop(productid, None)
    if not product:
        flash('Product not found', 'error')
    else:
        flash(f'Product "{product["name"]}" deleted successfully!', 'success')
    
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
