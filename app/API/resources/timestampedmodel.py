from flask import request
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import TimestampedModel, db

timestampedmodel_fields = Fields().timestampedmodel_fields()

class TimestampedModelListAPI(Resource):

    @marshal_with(timestampedmodel_fields)
    def get(self):
        timestampedmodels = TimestampedModel.query.all()
        return timestampedmodels

    @marshal_with(timestampedmodel_fields)
    def post(self):
        return {}


class TimestampedModelAPI(Resource):

    @marshal_with(timestampedmodel_fields)
    def get(self, id):
        timestampedmodel = TimestampedModel.query.get(id)
        return timestampedmodel

    @marshal_with(timestampedmodel_fields)
    def delete(self, id):
        timestampedmodel = TimestampedModel.query.get(id)
        db.session.delete(timestampedmodel)
        db.session.commit()
        timestampedmodels = TimestampedModel.query.all()
        return timestampedmodels

    @marshal_with(timestampedmodel_fields)
    def put(self, id):
        return {}