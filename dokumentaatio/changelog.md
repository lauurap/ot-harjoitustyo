## Viikko 3
- Luotu index ja tehty valikko
- Luotu game-luokka ja sinne aloitettu toiminnallisuutta
- Luotu board-luokka ja sinne laudan tulostus
- Testattu, että game-luokka asettaa nimen oikein

## Viikko 4
- Tehty board-luokkaan set_mark check_board_full ja check_win -metodit
- Pelaaja voi asettaa merkin haluamaansa kohtaan laudalla
- Peli loppuu tasapeliin, jos lauta on täynnä
- Peli loppuu, jos toinen pelaaja voittaa ja voittaja tunnistetaan
- Peli toimii nyt kahden ihmispelaajan kanssa oikein (vuoro ei vaihdu, vaikka pelaaja yrittää laittaa merkin väärään kohtaan)

## Viikko 5
- Tehty konepelaaja
- Testattu, että peli toimii oikein myös väärillä syötteillä

## Viikko 6
- Tallennus: pelin voi tallentaa ja sitä voi jatkaa myöhemmin

## Viikko 7
- Peli ei kaadu, jos kysyttäessä pelaako konetta vastaan vastaa jotain muuta kuin ei/kyllä
- Tallennuksen voi nollata suorittamalla python src/empty.py