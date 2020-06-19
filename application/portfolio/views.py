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
    p = Portfolio.query.filter_by(account_id = current_user.id).first()
    if p is None:
        p = Portfolio(id, 0,0,0,0)
        db.session().add(p)
        db.session().commit()
    portfolio = Portfolio.query.filter_by(account_id = current_user.id).first()
    transactions = Transaction.get_transactions()
    set_portfolio_balance(portfolio, transactions)
    btc = round(get_BTC_spotprice(),2)
    eth = round(get_ETH_spotprice(),2)
    link = round(get_LINK_spotprice(),2)
    xrp = round(get_XRP_spotprice(),2)
    balance_list = calculate_portfolio_value(btc, eth, link, xrp)
    return render_template("portfolio/view.html", balance_list = balance_list, portfolio=Portfolio.query.filter_by(account_id = current_user.id).first(),  btc = btc, eth = eth, link = link, xrp = xrp, transactions = transactions)

def calculate_portfolio_value(btc, eth, link, xrp):
    p = Portfolio.query.filter_by(account_id = current_user.id).first()
    btc_balance = round(btc * p.btc_amount,2)
    eth_balance =  round(eth * p.eth_amount,2)
    xrp_balance = round(xrp * p.xrp_amount,2)
    link_balance = round(link * p.link_amount,2)
    return [btc_balance, eth_balance, xrp_balance, link_balance]
def set_portfolio_balance(p, transactions):
    BTC = 0
    ETH = 0
    LINK = 0
    XRP = 0
    for transaction in transactions:
        if transaction.currency == "BTC":
            BTC = BTC + transaction.amount
        if transaction.currency == "ETH":
            ETH = ETH + transaction.amount
        if transaction.currency == "XRP":
            XRP = XRP + transaction.amount
        if transaction.currency == "LINK":
            LINK = LINK + transaction.amount
    p.btc_amount = int(BTC)
    p.eth_amount = int(ETH)
    p.xrp_amount = int(XRP)
    p.link_amount = int(LINK)
    db.session().commit()
def get_BTC_spotprice():
    responseBTC = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/spot")
    data = responseBTC.json()
    return float(data["data"]["amount"])
def get_ETH_spotprice():
    responseETH = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/spot")
    data = responseETH.json()
    return float(data["data"]["amount"])
def get_LINK_spotprice():
    responseETH = requests.get("https://api.coinbase.com/v2/prices/LINK-EUR/spot")
    data = responseETH.json()
    return float(data["data"]["amount"])
def get_XRP_spotprice():
    responseETH = requests.get("https://api.coinbase.com/v2/prices/XRP-EUR/spot")
    data = responseETH.json()
    return float(data["data"]["amount"])

