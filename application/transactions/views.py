from application import app, db
from flask import redirect, render_template, request, url_for
from application.transactions.models import Transaction

@app.route("/transactions", methods=["GET"])
def transactions_index():
    return render_template("transactions/list.html", transactions = Transaction.query.all())

@app.route("/transactions/new/")
def transactions_form():
    return render_template("transactions/new.html")


@app.route("/transactions/<transaction_id>/", methods=["POST"])
def transactions_set_done(transaction_id):

    t = Transaction.query.get(transaction_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("transactions_index"))

@app.route("/transactions/", methods=["POST"])
def transactions_create():
    t = Transaction(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("transactions_index"))