from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Sale, db
from application.forms.sale import CreateSaleForm, UpdateSaleForm, DeleteSaleForm, SearchSaleForm, FilterSaleForm 


sale_bp = Blueprint('sale_bp', __name__, url_prefix="/sale")


@sale_bp.route("/")
def get_Sales():
	Sales = Sale.query.all()
	return render_template('sale/Sales.html', Sales=Sales)


@sale_bp.route("/create", methods=['GET', 'POST'])
def create_sale():
	form = CreateSaleForm()
	if form.validate_on_submit():
		# register sale
		sale = Sale(
			)

		db.session.add()
		db.session.commit()
		id = sale.id
		return redirect(url_for('sale_bp.update_sale', id=id))
	return render_template('sale/create-sale.html', form=form)


@sale_bp.route("/<id>/update", methods=['GET', 'POST'])
def update_sale(id):
	sale = Sale.query.get(id)
	form = UpdateSaleForm(obj=sale)
	if form.validate_on_submit():
		# update sale

		db.session.commit()
		id = sale.id
		return redirect(url_for('sale_bp.update_sale', id=id))
	return render_template('sale/update-sale.html', form=form)


@sale_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_sale(id):
	sale = Sale.query.get(id)
	form = DeleteSaleForm(obj=sale)
	if form.validate_on_submit():
		db.session.delete()
		db.session.commit()
		return redirect(url_for('sale_bp.get_Sales'))
	return render_template('sale/delete-sale.html', form=form, sale=sale)


# secondary routes

