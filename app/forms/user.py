from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput
from app.models import User, Profile
from app.utils import authenticate_user


def unique_create_username(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(f"A user with username '{field.data}' already exists.")

def unique_create_email(form, field):
    if Profile.query.filter_by(email=field.data).first():
        raise ValidationError(f"A user with email '{field.data}' already exists.")


class CreateUserForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired(), Email(), unique_create_email])
	telephone = StringField(validators=[DataRequired()])
	username = StringField(validators=[DataRequired(), unique_create_username])
	password = StringField(validators=[DataRequired()])
	confirm_password = StringField(validators=[DataRequired()])


class UpdateUserPasswordForm(FlaskForm):
	current_password = StringField(validators=[DataRequired()])
	new_password = StringField(validators=[DataRequired()])
	confirm_password = StringField(validators=[DataRequired()])

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.user = user

	def validate_current_password(form, field):
		user = authenticate_user(form.user.username, field.data)
		if not user:
			raise ValidationError(f"Incorrect Current Password")
