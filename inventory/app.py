from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Location, ProductMovement

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# ---------------- PRODUCTS ----------------
@app.route('/products')
def view_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    db.session.add(Product(name=name))
    db.session.commit()
    return redirect(url_for('view_products'))

# ---------------- LOCATIONS ----------------
@app.route('/locations')
def view_locations():
    locations = Location.query.all()
    return render_template('locations.html', locations=locations)

@app.route('/add_location', methods=['POST'])
def add_location():
    name = request.form['name']
    db.session.add(Location(name=name))
    db.session.commit()
    return redirect(url_for('view_locations'))

# ---------------- MOVEMENTS ----------------
@app.route('/movements')
def view_movements():
    movements = ProductMovement.query.all()
    products = Product.query.all()
    locations = Location.query.all()
    return render_template('movements.html', movements=movements, products=products, locations=locations)

@app.route('/add_movement', methods=['POST'])
def add_movement():
    product_id = request.form['product_id']
    qty = int(request.form['qty'])
    from_location = request.form.get('from_location') or None
    to_location = request.form.get('to_location') or None

    db.session.add(ProductMovement(
        product_id=product_id,
        qty=qty,
        from_location=from_location if from_location else None,
        to_location=to_location if to_location else None
    ))
    db.session.commit()
    return redirect(url_for('view_movements'))

# ---------------- REPORT ----------------
@app.route('/report')
def report():
    products = Product.query.all()
    locations = Location.query.all()
    balances = []

    for product in products:
        for loc in locations:
            incoming = db.session.query(db.func.sum(ProductMovement.qty)).filter_by(product_id=product.product_id, to_location=loc.location_id).scalar() or 0
            outgoing = db.session.query(db.func.sum(ProductMovement.qty)).filter_by(product_id=product.product_id, from_location=loc.location_id).scalar() or 0
            balance = incoming - outgoing
            balances.append({
                'product': product.name,
                'location': loc.name,
                'qty': balance
            })

    return render_template('report.html', balances=balances)

if __name__ == '__main__':
    app.run(debug=True)
