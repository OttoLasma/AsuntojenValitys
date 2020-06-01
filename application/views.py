from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    list = User.find_user_with_largest_BTC_transaction()
    return render_template("index.html", list = list)
