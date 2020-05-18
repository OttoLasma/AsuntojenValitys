from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for

from application.transactions.models import Transaction
from application.transactions.forms import TransactionForm, TransactionEditForm
from application import app, db


@app.route("/transactions", methods=["GET"])
@login_required
def transactions_index():
    return render_template("transactions/list.html", transactions=Transaction.query.filter_by(account_id = current_user.id))

@app.route("/transactions/new/")
@login_required
def transactions_form():
    return render_template("transactions/new.html", form=TransactionForm())



@app.route("/transactions/", methods=["GET", "POST"])
@login_required
def transactions_create():
    form = TransactionForm(request.form)
    if not form.validate():
        return render_template("transactions/new.html", form=form)
    t = Transaction(form.currency.data, form.amount.data)
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/transactions/edit/<transaction_id>", methods=["GET", "POST"])
@login_required
def edit_transaction(transaction_id):
    if request.method == "GET":
        transaction = Transaction.query.get(transaction_id)
        form = TransactionEditForm(currency = transaction.currency, amount = transaction.amount)
        return render_template("transactions/edit.html", form = form)
    form = TransactionEditForm(request.form)
    transaction = Transaction.query.get(transaction_id)
    if not form.validate():
        return render_template("transactions/edit.html", form=form)
    transaction.currency = form.currency.data
    transaction.amount = form.amount.data
    db.session().commit()
    return redirect(url_for("transactions/list.html"))

@app.route("/transactions/delete/<transaction_id>", methods=["POST"])
@login_required
def delete_transaction(transaction_id):
    Transaction.query.filter_by(id = transaction_id).delete()
    db.session().commit()
    return render_template("transactions/list.html", transactions=Transaction.query.filter_by(account_id = current_user.id))