from flask import request
from sqlalchemy import desc
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import SaleGroup, db

sale_group_fields = Fields().sale_group_fields()

class SaleGroupListAPI(Resource):

    @marshal_with(sale_group_fields)
    def get(self):
        user_id = request.args.get("user")
        query = SaleGroup.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        query = query.order_by(desc(SaleGroup.created_at))
        return query.all()

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