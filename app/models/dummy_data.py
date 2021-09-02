from app.models import *
from app import db


roles = [
	{"name": "admin"},
	{"name": "cashier"},
]

users = [
    {"username": "samit", "password":"123", "is_active":True, "roles":["admin"]},
    {"username": "samuelitwaru", "password":"123", "is_active":True, "roles":["cashier"]},
]


profiles = [
	{"name": "Samuel Itwaru", "email": "samuelitwaru@gmail.com", "telephone": "256-781902516"},
	{"name": "Samuel Itwaru", "email": "samuelitwaru@yahoo.com", "telephone": "256-752041475"}
]


def create_roles():
	index = 0
	for role in roles:
		r = Role(name=role["name"])
		db.session.add(r)
		roles[index]["model"] = r
		index += 1
	db.session.commit()


def create_users():
	index = 0
	for user in users:
		profile = profiles[index]
		user_obj = User(username=user["username"], password=user["password"], is_active=user["is_active"])
		profile = Profile(name=profile["name"], email=profile["email"], telephone=profile["telephone"])
		user_obj.profile = profile
		user_obj.set_roles(user["roles"])
		db.session.add(user_obj)
		db.session.add(profile)
		index += 1
	db.session.commit()



def main(should_create_users):
	create_roles()
	if should_create_users:
		create_users()