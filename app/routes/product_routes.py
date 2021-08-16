from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Product, db
from application.forms.product import CreateProductForm, UpdateProductForm, DeleteProductForm, SearchProductForm, FilterProductForm 


product_bp = Blueprint('product_bp', __name__, url_prefix="/product")


@product_bp.route("/")
def get_products():
	Products = Product.query.all()
	return render_template('product/Products.html', Products=Products)


@product_bp.route("/create", methods=['GET', 'POST'])
def create_product():
	form = CreateProductForm()
	if form.validate_on_submit():
		# register product
		product = Product(
			)

		db.session.add()
		db.session.commit()
		id = product.id
		return redirect(url_for('product_bp.update_product', id=id))
	return render_template('product/create-product.html', form=form)


@product_bp.route("/<id>/update", methods=['GET', 'POST'])
def update_product(id):
	product = Product.query.get(id)
	form = UpdateProductForm(obj=product)
	if form.validate_on_submit():
		# update product

		db.session.commit()
		id = product.id
		return redirect(url_for('product_bp.update_product', id=id))
	return render_template('product/update-product.html', form=form)


@product_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_product(id):
	product = Product.query.get(id)
	form = DeleteProductForm(obj=product)
	if form.validate_on_submit():
		db.session.delete()
		db.session.commit()
		return redirect(url_for('product_bp.get_Products'))
	return render_template('product/delete-product.html', form=form, product=product)


# secondary routes







@product_bp.route("/<id>/stock")
def get_product_stock():
	product = Product.query.get(id)
	stock = product.stock
	return render_template('stock/secondary-stock.html', parent_template='product/product.html', product=product, stock=stock)



@product_bp.route("/<id>/sales")
def get_product_sales():
	product = Product.query.get(id)
	sales = product.sales
	return render_template('sale/secondary-sales.html', parent_template='product/product.html', product=product, sales=sales)



