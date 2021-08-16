from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import HiddenInput


class CreateStockForm(FlaskForm):
    submit = SubmitField('Register')


class UpdateStockForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Update')


class DeleteStockForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


class SearchStockForm(FlaskForm):
    query = StringField("Search")
    submit = SubmitField('Search')


class FilterStockForm(FlaskForm):
    submit = SubmitField('Filter')