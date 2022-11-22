# Ohjelmistotekniikka, harjoitustyö

## Ristinolla

Ristinolla-pelissä pelaajien on mahdollista pelata perinteistä ristinollaa. Tarkoitus on, että pelissä pystyy valitsemaan, pelaako toista ihmistä vai konetta vastaan. Pelissä olisi tarkoitus myös päästä valitsemaan pelilaudan koko. Vielä nyt peli on pahasti kesken.

### Python-versio

Harjoitustyö on testattu Python 3.8 -versiolla

### Dokumentaatio

[changelog.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[tyoaikakirjanpito.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[vaatimusmaarittely.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Asennus

1. poetry install asentaa riippuvuudet
 
2. poetry run invoke start käynnistää ristinolla-pelin

### Komentorivitoiminnot

1. poetry run invoke start käynnistää ristinolla-pelin

2. poetry run invoke test suorittaa testit

3. poetry run invoke coverage_report kerää testikattavuuden ja muodostaa HTML-raportin



