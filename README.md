# Virtuaalivaluuttasalkku 

Tarkoituksena on laatia alusta, jossa käyttäjät voivat tarkastella omien virtuaalivaluuttoihin tehtyjen sijoituksien arvoa. Käyttäjät jaetaan alustavasti kahteen ryhmään: käyttäjät, sekä alustan ylläpitäjät. Käyttäjä ilmoittaa omistuksensa ja ostohinnan kustakin määritetystä virtuaalivaluutasta ja alustan olisi tarkoitus näyttää visuaalisesti käyttäjän portfolion kehittyminen. Mikäli en edellä esitettyyn vaadittua määrää tauluja, voi kaikkien määritettyjen virtuaalivaluuttojen alle kommentoida oman mielipiteen kyseisestä virtuaalivaluutasta. 

<h1> Halutut toiminnot </h1>

- Kijautuminen (valmis)
- Käyttäjän luominen (valmis)
- Oman portfolion päivittäminen (valmis)
- Portfolion kehityksen seuraaminen (osittain valmis)

# Linkin muuhun dokumentaatioon:

[Linkki tietokantakaavioon](https://github.com/OttoLasma/VirtuaalivaluuttaPortfolio/blob/master/documentation/Screenshot%20from%202020-05-13%2020-04-25.png)

[Linkki herokuun](https://tsoha-cryptoportfolio.herokuapp.com/)

[Linkki user storyihin](https://github.com/OttoLasma/VirtuaalivaluuttaPortfolio/blob/master/documentation/userstory.md)

<h1> Asennusohje </h1>

Sovelluksen suorittamiseen lokaalista koneelaesi täytyy olla ladattuna ainakin seuraavat:

- `python3`
- `venv`
- `pip`
- `sqlite`

Lataa sovellus koneellesi tai suorita komento `git clone https://github.com/OttoLasma/VirtuaalivaluuttaPortfolio`. Tämän jälkeen suorita vielä seuraavat komennot:

- `python3 -m venv venv`
- `source venve/bin/activate`
- `pip install requirements.txt`
- `python run.py`

Nyt sovellus on tarkasteltavissa osoitteessa http://localhost:5000. 

