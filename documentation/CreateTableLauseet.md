# CREATE TABLE -lauseet

## User 
```SQL
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id))
```
## Transaction
```SQL
CREATE TABLE "transaction" (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        currency VARCHAR(144) NOT NULL, 
        amount INTEGER NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id))
```

## Portfolio
```SQL
CREATE TABLE portfolio (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        btc_amount INTEGER, 
        eth_amount INTEGER, 
        xrp_amount INTEGER, 
        link_amount INTEGER, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id))
```
