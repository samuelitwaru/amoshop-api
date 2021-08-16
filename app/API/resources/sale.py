from flask import request, redirect, url_for
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import Sale, Product, SaleGroup, User, db
from app.forms import CreateSaleForm

sale_fields = Fields().sale_fields()

class SaleListAPI(Resource):

    @marshal_with(sale_fields)
    def get(self):
        sales = Sale.query.all()
        return sales

    @marshal_with(sale_fields)
    def post(self):
        return {}


class SaleAPI(Resource):

    @marshal_with(sale_fields)
    def get(self, id):
        sale = Sale.query.get(id)
        return sale

    @marshal_with(sale_fields)
    def delete(self, id):
        sale = Sale.query.get(id)
        db.session.delete(sale)
        db.session.commit()
        sales = Sale.query.all()
        return sales

    @marshal_with(sale_fields)
    def put(self, id):
        return {}


class SaleCheckoutAPI(Resource):

    @marshal_with(sale_fields)
    def post(self):
        data = request.json
        amount = data.get("amount")
        paid = data.get("paid")
        sales = data.get("cart")
        sale_models = []

        for product_id, sale in sales.items():
            product = Product.query.filter_by(id=product_id).first()

            create_sale_form = CreateSaleForm(data={"quantity":sale.get("quantity")}, meta={'csrf': False})
            
            if create_sale_form.validate_on_submit():
                data = create_sale_form.data
                quantity = data.get("quantity")
                sale = Sale(quantity=quantity, buying_price=product.buying_price, selling_price=product.selling_price, product_id=product_id)
                sale_models.append(sale)

        current_user = User.query.filter_by(token=request.args.get("token")).first()
        sale_group = SaleGroup(amount=amount, paid=paid, user_id=current_user.id)
        sale_group.sales = sale_models
        
        db.session.add_all(sale_models)
        db.session.add(sale_group)

        db.session.commit()
        db.session.close()

        return SaleListAPI.get(SaleListAPI)