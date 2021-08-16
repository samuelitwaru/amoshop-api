from flask import request
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import Stock, db

stock_fields = Fields().stock_fields()

class StockListAPI(Resource):

    @marshal_with(stock_fields)
    def get(self):
        stocks = Stock.query.all()
        return stocks

    @marshal_with(stock_fields)
    def post(self):
        return {}


class StockAPI(Resource):

    @marshal_with(stock_fields)
    def get(self, id):
        stock = Stock.query.get(id)
        return stock

    @marshal_with(stock_fields)
    def delete(self, id):
        stock = Stock.query.get(id)
        db.session.delete(stock)
        db.session.commit()
        stocks = Stock.query.all()
        return stocks

    @marshal_with(stock_fields)
    def put(self, id):
        return {}