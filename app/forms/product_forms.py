from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput
from app.models import Product


def unique_create_barcode(form, field):
    if field.data:
        if Product.query.filter_by(barcode=field.data).first():
            raise ValidationError(f"A product with barcode '{field.data}' already exists.")
    else:
    	field.data = None

def unique_update_barcode(form, field):
	if field.data:
	    if Product.query.filter(Product.id!=form.id.data).filter_by(barcode=field.data).first():
	        raise ValidationError(f"A product with barcode '{field.data}' already exists.")
	else:
	    field.data = None


class CreateProductForm(FlaskForm):
	name = StringField(validators=[DataRequired()])
	brand = StringField(validators=[])
	description = StringField(validators=[])
	barcode = StringField(validators=[unique_create_barcode])
	selling_price = IntegerField(validators=[DataRequired()])
	buying_price = IntegerField(validators=[DataRequired()])
	units = StringField(validators=[DataRequired()])


class UpdateProductForm(FlaskForm):
	id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
	name = StringField(validators=[DataRequired()])
	brand = StringField(validators=[])
	description = StringField(validators=[])
	barcode = StringField(validators=[unique_update_barcode])
	selling_price = IntegerField(validators=[DataRequired()])
	buying_price = IntegerField(validators=[DataRequired()])
	units = StringField(validators=[DataRequired()])
	submit = SubmitField('Update')


class DeleteProductForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


class SearchProductForm(FlaskForm):
    query = StringField("Search")
    submit = SubmitField('Search')


class FilterProductForm(FlaskForm):
    submit = SubmitField('Filter')