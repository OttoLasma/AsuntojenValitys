from flask_login import login_required
from flask import redirect, render_template, request, url_for

from application.transactions.models import Transaction
from application.transactions.forms import TransactionForm
from application import app, db

@app.route("/transactions", methods=["GET"])
def transactions_index():
    return render_template("transactions/list.html", transactions = Transaction.query.all())

@app.route("/transactions/new/")
@login_required
def transactions_form():
    return render_template("transactions/new.html", form = TransactionForm())


@app.route("/transactions/<transaction_id>/", methods=["POST"])
@login_required
def transactions_set_done(transaction_id):

    t = Transaction.query.get(transaction_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("transactions_index"))

@app.route("/transactions/", methods=["POST"])
@login_required
def transactions_create():
    form = TransactionForm(request.form)
    if not form.validate():
        return render_template("transactions/new.html", form = form)
    t = Transaction(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    
  
    return redirect(url_for("transactions_index"))