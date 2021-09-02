from flask import request
from flask_restful import Resource, marshal_with
from ..fields import Fields
from app.models.models import Category, db
from app.forms import CreateCategoryForm, UpdateCategoryForm
from app.utils import output_json


category_fields = Fields().category_fields()


class CategoryListAPI(Resource):

    @marshal_with(category_fields)
    def get(self):
        categorys = Category.query.all()
        return categorys

    def post(self):
        data = request.json
        create_category_form = CreateCategoryForm(data=data, meta={"csrf":False})
        if create_category_form.validate_on_submit():
            name = data.get("name")
            category = Category(name=name)
            db.session.add(category)
            db.session.commit()
            return self.get()
        else:
            return output_json({"message":create_category_form.errors}, 406)


class CategoryAPI(Resource):

    @marshal_with(category_fields)
    def get(self, id):
        category = Category.query.get(id)
        return category

    @marshal_with(category_fields)
    def delete(self, id):
        category = Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        categorys = Category.query.all()
        return categorys

    def put(self, id):
        category = Category.query.get(id)
        data = request.json
        data["id"] = id
        update_category_form = UpdateCategoryForm(data=data, meta={"csrf":False})
        if update_category_form.validate_on_submit():
            category.name = data.get("name")
            db.session.commit()
            return CategoryListAPI.get(CategoryListAPI)
        else:
            return output_json({"message":update_category_form.errors}, 406)
