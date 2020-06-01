<h1> Nykyiset user storyt </h1>

* Käyttäjänä haluan korjata kirjauksia, sillä virheelliset kirjaukset vääristäisivät saldoa
* Käyttäjänä haluan poistaa kirjauksia, sillä virheelliset/väärät kirjaukset vääristävät saldoa
* Käyttäjänä haluan kirjautua, jotta voin tarkastella omia kirjauksiani
* Käyttäjänä haluan kirjautua ulos, jotta kukaan ei pääse näkemään saldoani/kirjauksiani
* Käyttäjänä haluan tietää ajankohtaiset virtuaalivaluuttojen hinnat, jotta voin seurata saldoni kehitysta
* Käyttäjänä haluan(?) tietää muiden käyttäjien nimet, mikäli heillä on yli 127 btc/miljoonan euron edestä kyseistä valuuttaa
find_user_with_largest_BTC_transaction():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Portfolio ON Portfolio.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Portfolio.btc_amount) > 127")
