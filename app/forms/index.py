from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput
from app.models import Product


class ResetDBForm(FlaskForm):
	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])