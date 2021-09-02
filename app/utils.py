import json
from flask import make_response
from werkzeug.security import check_password_hash
from itsdangerous import Serializer
from app.models import *
from app import app, db, api
from app.models.dummy_data import create_roles


def authenticate_user(username, password):
	user = User.query.filter_by(username=username).first()
	if user and user.password and check_password_hash(user.password, password):
		return user
	return None


def create_user_token(user, token_period=3600):
	s = Serializer(app.config['SECRET_KEY'])
	token = s.dumps({ 'id': user.id })
	user.token = token
	db.session.commit()


@api.representation('application/json')
def output_json(data, code, headers=None):
	"""Makes a Flask response with a JSON encoded body"""
	resp = make_response(json.dumps(data), code)
	resp.headers.extend(headers or {})
	return resp


def reset_db():
	for user in User.query.all():
		user.roles = []
	for role in User.query.all():
		role.users = []

	User.query.delete()
	Role.query.delete()
	Profile.query.delete()
	
	Sale.query.delete()
	SaleGroup.query.delete()
	Stock.query.delete()
	
	for product in Product.query.all():
		product.categories = []
	for category in Category.query.all():
		category.products = []
	Product.query.delete()
	Category.query.delete()
	create_roles()


	db.session.commit()