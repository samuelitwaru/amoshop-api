from flask import request
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import SaleGroup, db

sale_group_fields = Fields().sale_group_fields()

class SaleGroupListAPI(Resource):

    @marshal_with(sale_group_fields)
    def get(self):
        sale_groups = SaleGroup.query.all()
        return sale_groups

    @marshal_with(sale_group_fields)
    def post(self):
        return {}


class SaleGroupAPI(Resource):

    @marshal_with(sale_group_fields)
    def get(self, id):
        sale_group = SaleGroup.query.get(id)
        return sale_group

    @marshal_with(sale_group_fields)
    def delete(self, id):
        sale_group = SaleGroup.query.get(id)
        db.session.delete(sale_group)
        db.session.commit()
        sale_groups = SaleGroup.query.all()
        return sale_groups

    @marshal_with(sale_group_fields)
    def put(self, id):
        return {}