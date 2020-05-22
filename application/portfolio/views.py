from application import app, db
from application.transactions.models import Transaction
from application.portfolio.models import Portfolio

from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for
import requests
import json




@app.route("/portfolio", methods=["GET"])
@login_required
def portfolio_index():
    print("MODMDOMDODODMDOMDOMDOMDODMDOMDOMOMDMDOMDOMOMDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    id = current_user.id
    p = Portfolio.query.filter_by(account_id = current_user.id).first()
    if p is None:
        p = Portfolio(id, 0,0)
        db.session().add(p)
        db.session().commit()
    p = Portfolio.query.filter_by(account_id = current_user.id).first()
    transactions = Transaction.get_transactions()
    calculate_value(p, transactions)
    return render_template("portfolio/view.html", portfolio=Portfolio.query.filter_by(account_id = current_user.id).first())

def calculate_value(p, transactions):
    BTC = 0
    ETH = 0
    for transaction in transactions:
        if transaction.currency == "BTC":
            BTC = BTC + transaction.amount
        if transaction.currency == "ETH":
            ETH = ETH + transaction.amount
    p.btc_amount = int(BTC * get_BTC_spotprice())
    p.eth_amount = int(ETH * get_ETH_spotprice())
    db.session().commit()
def get_BTC_spotprice():
    responseBTC = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/spot")
    data = responseBTC.json()
    return float(data["data"]["amount"])
def get_ETH_spotprice():
    responseETH = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/spot")
    data = responseETH.json()
    return float(data["data"]["amount"])

