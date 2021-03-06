from flask import request
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import Product, Category, db
from app.forms import CreateProductForm, UpdateProductForm
from app.utils import output_json


product_fields = Fields().product_fields()


class ProductListAPI(Resource):

    @marshal_with(product_fields)
    def get(self):
        query_string = request.args.get("search")
        if query_string:
            query = Product.query.filter(Product.barcode==query_string)
            if not query.first():
                query = Product.query.filter(Product.name.like(f'%{query_string}%'))
            return query.all()
        products = Product.query.all()
        return products

    def post(self):
        req_data = request.json
        create_product_form = CreateProductForm(data=req_data, meta={"csrf":False})
        if create_product_form.validate_on_submit():
            data = create_product_form.data
            name = data.get("name")
            brand = data.get("brand")
            description = data.get("description")
            barcode = data.get("barcode")
            buying_price = data.get("buying_price")
            selling_price = data.get("selling_price")
            units = data.get("units")
            
            product = Product(
                name=name, brand=brand, description=description, 
                barcode=barcode, buying_price=buying_price, 
                selling_price=selling_price, units=units
                )

            category_ids = req_data.get("categories")
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            product.categories = categories

            db.session.add(product)
            db.session.commit()
            db.session.close()
        else:
            return output_json({"message":create_product_form.errors}, 406)
        return self.get()


class ProductAPI(Resource):

    @marshal_with(product_fields)
    def get(self, id):
        product = Product.query.get(id)
        return product

    @marshal_with(product_fields)
    def delete(self, id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        products = Product.query.all()
        return products

    def put(self, id):
        product = Product.query.filter_by(id=id).first()
        req_data = request.json
        req_data["id"] = id
        update_product_form = UpdateProductForm(data=req_data, meta={"csrf":False})
        if update_product_form.validate_on_submit():
            data = update_product_form.data
            name = data.get("name")
            brand = data.get("brand")
            description = data.get("description")
            barcode = data.get("barcode")
            buying_price = data.get("buying_price")
            selling_price = data.get("selling_price")
            units = data.get("units")

            product.name = name
            product.brand =brand
            product.description = description
            product.barcode = barcode
            product.buying_price = buying_price
            product.selling_price = selling_price
            product.units = units

            category_ids = req_data.get("categories")
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            product.categories = categories

            db.session.commit()
            db.session.close()
        else:
            return output_json({"message":update_product_form.errors}, 406)
        return ProductListAPI.get(ProductListAPI)


class ProductQuantityAPI(Resource):

    def put(self, id):
        product = Product.query.filter_by(id=id).first()
        data = request.json
        quantity = data.get("quantity")
        product.quantity += quantity
        db.session.commit()
        return ProductListAPI.get(ProductListAPI)