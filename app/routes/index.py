from flask import Blueprint, request, render_template, redirect, url_for, flash, send_file
from app.models import db
from app.forms import ResetDBForm
from app.utils import authenticate_user, reset_db


index_bp = Blueprint('index', __name__, url_prefix="/")


@index_bp.route("/")
def index():
	reset_db_form = ResetDBForm()
	return render_template('index/index.html', reset_db_form=reset_db_form)



@index_bp.route("/reset", methods=["POST"])
def reset():
	reset_db_form = ResetDBForm()
	if reset_db_form.validate_on_submit():
		data = reset_db_form.data
		username = data.get("username")
		password = data.get("password")
		user = authenticate_user(username, password)
		if user:
			# reset db
			reset_db()
			flash("Database reset", "success")
		else:
			flash("Invalid credentials", "danger")
	return redirect(url_for('index.index'))


@index_bp.route("/download/linux-64")
def download_lin_64():
	return send_file(f"media/amoshop-lin64.zip",
                     attachment_filename="amoshop-lin64.zip", as_attachment=True,
                     cache_timeout=0)


@index_bp.route("/download/win-64")
def download_win_64():
	return send_file(f"media/amoshop-win64.exe",
                     attachment_filename="amoshop-win64.exe", as_attachment=True,
                     cache_timeout=0)