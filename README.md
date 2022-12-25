# Ohjelmistotekniikka, harjoitustyö

# Ristinolla

Ristinolla-pelissä pelaajien on mahdollista pelata perinteistä ristinollaa. Pelin tarkoitus
on saada pelilaudalle kolme omaa merkkiä peräkkäin joko vaaka-, pysty- tai diagonaalisessa
suunnassa. Pelaaja voi valita, pelaako hän konetta vai toista ihmispelaajaa vastaan. 
Pelin pystyy tallentamaan ja jatkamaan myöhemmin.

[Loppupalautus release](https://github.com/lauurap/ot-harjoitustyo/releases/tag/loppupalautus)

[Viikon 6 release](https://github.com/lauurap/ot-harjoitustyo/releases/tag/viikko6)

[Viikon 5 release](https://github.com/lauurap/ot-harjoitustyo/releases/tag/viikko5)

## Python-versio

Peli on testattu Python 3.8 -versiolla. Pelin toimivuus on testattu
laitoksen koneella käyttämällä etätyöpöytää. 

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](./dokumentaatio/testaus.md)

- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](./dokumentaatio/changelog.md)


## Asennus

Lataa loppupalautus release zip-tiedosto ja pura se. Tee seuraavat komennot komentorivillä:

1. Asenna riippuvuudet:
```bash
poetry install
```
 
2. Suorita tallennetun pelin tyhjennys:
```bash
poetry run invoke empty
```

3. Käynnistä peli:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Pelin käynnistäminen

Pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Testikattavuusraportti löytyy _htmlcov_-hakemiston _index.html_-tiedostosta.

### Pylint

[.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```



