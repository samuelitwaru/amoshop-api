from flask import request
from flask_restful import Resource, marshal_with, marshal
from flask_login import login_user, logout_user
from ..fields import Fields
from app.utils import authenticate_user, create_user_token, output_json
from app.models.models import User, Profile, Role, db
from app.forms import CreateUserForm, UpdateUserPasswordForm
from app import api
user_fields = Fields().user_fields()
session_fields = Fields().session_fields()


class UserListAPI(Resource):

    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    def post(self):
        req_data = request.json
        create_user_form = CreateUserForm(data=req_data, meta={"csrf":False})
        if create_user_form.validate_on_submit():
            data = create_user_form.data
            name = data.get("name")
            email = data.get("email")
            telephone = data.get("telephone")
            username = data.get("username")
            password = data.get("password")
            is_active = data.get("is_active", True)
            
            user = User(username=username, password=password, is_active=is_active)
            profile = Profile(name=name, email=email, telephone=telephone)
            db.session.add(user)
            db.session.add(profile)
            user.profile = profile
            role_names = req_data.get("roles")
            roles = Role.query.filter(Role.name.in_(role_names)).all()
            user.roles = roles
            db.session.commit()
            db.session.close()
        else:
            return output_json({"message":create_user_form.errors}, 406)
        return self.get()


class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        user = User.query.get(id)
        return user

    @marshal_with(user_fields)
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def put(self, id):
        data = request.json
        user = User.query.filter_by(id=id)
        print(data)
        user.update(data)
        db.session.commit()
        return UserListAPI.get(UserListAPI)


class UserAuthAPI(Resource):

    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")
        user = authenticate_user(username, password)
        if user:
            if user.is_active:
                token = user.generate_auth_token()
                user.token = token.decode()
                db.session.commit()
                return marshal(user, user_fields)
            else:
                return output_json({"message":"Access denied! Your account is inactive."}, 406)
        return output_json({"message":"Incorrect username and password combination!"}, 406)


class UserUpdateAPI(Resource):

    # @marshal_with(user_fields)
    def put(self, id):
        data = request.json
        user = User.query.get(id)
        current_password = data.get("current_password")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")
        update_user_password_form = UpdateUserPasswordForm(data=data, user=user, meta={"csrf":False})
        if update_user_password_form.validate_on_submit():
            data = update_user_password_form.data
            password = data.get("new_password")
            user.set_password(password)
            db.session.commit()
            return marshal(user, user_fields)
        else:
            return output_json({"message": update_user_password_form.errors}, 406)
