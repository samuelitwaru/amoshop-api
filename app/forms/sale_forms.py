from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput


class CreateSaleForm(FlaskForm):
	quantity = IntegerField(validators=[DataRequired()])


class UpdateSaleForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Update')


class DeleteSaleForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


class SearchSaleForm(FlaskForm):
    query = StringField("Search")
    submit = SubmitField('Search')


class FilterSaleForm(FlaskForm):
    submit = SubmitField('Filter')