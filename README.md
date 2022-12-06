# Ohjelmistotekniikka, harjoitustyö

## Ristinolla

Ristinolla-pelissä pelaajien on mahdollista pelata perinteistä ristinollaa. 
Pelaaja voi valita, pelaako hän konetta vai toista ihmispelaajaa vastaan. 
Tallennusmahdollisuus on myös tulossa.

[Viikon 5 release](https://github.com/lauurap/ot-harjoitustyo/releases/tag/viikko5)

### Python-versio

Harjoitustyö on testattu Python 3.8 -versiolla

### Dokumentaatio

[changelog.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[tyoaikakirjanpito.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[vaatimusmaarittely.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuuri.md](https://github.com/lauurap/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Asennus

1. poetry install asentaa riippuvuudet
 
2. poetry run invoke start käynnistää ristinolla-pelin

### Komentorivitoiminnot

1. poetry run invoke start käynnistää ristinolla-pelin

2. poetry run invoke test suorittaa testit

3. poetry run invoke coverage-report kerää testikattavuuden ja muodostaa HTML-raportin

4. poetry run invoke lint suorittaa .pylintrc:n tarkistukset



