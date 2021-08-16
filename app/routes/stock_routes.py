from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Stock, db
from application.forms.stock import CreateStockForm, UpdateStockForm, DeleteStockForm, SearchStockForm, FilterStockForm 


stock_bp = Blueprint('stock_bp', __name__, url_prefix="/stock")


@stock_bp.route("/")
def get_Stocks():
	Stocks = Stock.query.all()
	return render_template('stock/Stocks.html', Stocks=Stocks)


@stock_bp.route("/create", methods=['GET', 'POST'])
def create_stock():
	form = CreateStockForm()
	if form.validate_on_submit():
		# register stock
		stock = Stock(
			)

		db.session.add()
		db.session.commit()
		id = stock.id
		return redirect(url_for('stock_bp.update_stock', id=id))
	return render_template('stock/create-stock.html', form=form)


@stock_bp.route("/<id>/update", methods=['GET', 'POST'])
def update_stock(id):
	stock = Stock.query.get(id)
	form = UpdateStockForm(obj=stock)
	if form.validate_on_submit():
		# update stock

		db.session.commit()
		id = stock.id
		return redirect(url_for('stock_bp.update_stock', id=id))
	return render_template('stock/update-stock.html', form=form)


@stock_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_stock(id):
	stock = Stock.query.get(id)
	form = DeleteStockForm(obj=stock)
	if form.validate_on_submit():
		db.session.delete()
		db.session.commit()
		return redirect(url_for('stock_bp.get_Stocks'))
	return render_template('stock/delete-stock.html', form=form, stock=stock)


# secondary routes

