from flask import render_template
from application import app, db
from application.auth.models import User
from flask_login import login_required, current_user
from sqlalchemy.sql import text

@app.route("/")
def index():
    return render_template("index.html")
