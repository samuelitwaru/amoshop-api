from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput
from app.models import Category


def unique_create_name(form, field):
    if field.data:
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError(f"A category with name '{field.data}' already exists.")
    else:
    	field.data = None

def unique_update_name(form, field):
	if field.data:
	    if Category.query.filter(Category.id!=form.id.data).filter_by(name=field.data).first():
	        raise ValidationError(f"A category with name '{field.data}' already exists.")
	else:
	    field.data = None


class CreateCategoryForm(FlaskForm):
	name = StringField(validators=[DataRequired(), unique_create_name])
	

class UpdateCategoryForm(FlaskForm):
	id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
	name = StringField(validators=[DataRequired(), unique_update_name])
