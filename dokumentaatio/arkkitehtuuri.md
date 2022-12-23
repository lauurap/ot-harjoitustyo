# Arkkitehtuuri

## Rakenne

Koodin pakkausrakenne on alla: 

![](./kuvat/pakkausrakenne1.PNG)

Pakkaus _ui_ sisältää käyttöliittymän koodin ja _services_ sisältää sovelluslogiikan koodin, eli luokat Game, Board, 
Humanplayer ja Computerplayer. _Repositories_ vastaa tietojen tallentamisen tiedostoon ja tietojen lukemisen tiedostosta.

## Käyttöliittymä

Kun peli käynnistetään, avautuu valikko, jonka näyttämisestä vastaa TicTacToe-luokka. Jos halutaan aloittaa uusi peli,
TicTacToe luo services-pakkauksessa olevan Game-olion ja kutsuu Game-luokan metodeja. 

Jos halutaan jatkaa aiemmin tallennettua peliä, TicTacToe luo repositories-pakkauksen GameRepository-olion ja kutsuu 
GameRepository-luokan metodeja, jolloin tallennetun pelin tiedot saadaan luotua. Tämän jälkeen TicTacToe luo 
services-pakkauksessa olevan Game-olion ja kutsuu Game-luokan metodeja.

## Sovelluslogiikka 

Sovelluslogiikan muodostavat luokat Game, Board, Humanplayer ja Computerplayer. Ristinolla-pelissä Game-luokka 
kutsuu pelaamisessa Board-, Humanplayer- ja Computerplayer-luokan metodeja. Alla on pelin rakennetta kuvaava luokkakaavio.

```mermaid
 classDiagram
      Board <|-- Game
      Humanplayer <|-- Game
      Computerplayer <|-- Game
      class Board{
          name1
          name2
          numberstring
          numbers
          numberstring_to_numbers(number_string)
          print_board()
          check_place_free(place, turn)
          set_mark(mark, place)
          check_win()
          check_board_full()

      }
      class Game{
          name1
          name2
          turn
          numberstring
          play_game()
          game_is_finished(turn, board)
      }
      class Humanplayer{
          name
          mark
          do_turn(board, place)
          ask_place(board, turn)
          do_turns(board, turn)
      }
      class Computerplayer{
          name
          mark
          do_turn(board)
      }
```

## Pelin tallennus

Pakkauksen repositories luokka GameRepository vastaa pelin tallentamisesta. GameRepositoryn metodi store tallentaa pelin
pelaajat, vuorossa olevan pelaajan ja pelilaudan tiedostoon. GameRepositoryn metodi read lukee tiedostosta vastaavat tiedot. 

### Tiedostot

Peli tallettaa pelaajien nimet, pelilaudan ja vuorossa olevan pelaajan tiedot erilliseen
tekstitiedostoon seuraavassa formaatissa:
```bash
name1
name2
 123456789
1
```
Seuraava vuorossa olevaa pelaaja kuvataan joko numerolla 1 tai 2. 1 tarkoittaa, että ensimmäisenä
nimensä antanut pelaaja pelaa seuraavaksi. 

## Toiminnallisuus

### Uuden pelin aloittaminen
Uuden pelin aloittaminen alkaa kirjoittamalla aloitusvalikkoon "a", 
jonka jälkeen kirjoitetaan pelaajan nimi. Seuraavaksi valitaan, pelataanko
tietokonetta vai toista ihmispelaajaa vastaan. 
Alla oleva sekvenssikaavio kuvaa, miten peli etenee, kun kaksi ihmispelaajaa
pelaa keskenään. 

```mermaid
 sequenceDiagram
      TicTacToe ->> Game : play_game()

      loop while game_is_finished() return False
          Game ->> HumanPlayer : do_turns()
          HumanPlayer ->> Board : check_place_free()
          Board --> HumanPlayer : True
          HumanPlayer ->> Board : set_mark()
          Board --> HumanPlayer : True
          HumanPlayer -->> Game : True
          Game --> Game : change turn
      end
```
Eli kun pelaaja on valinnut pelaavansa peliä toista ihmispelaajaa vastaan ja kun molemmat ovat
syöttäneet nimensä, luodaan uusi Game- ja Board-olio. Game-luokan play_game-metodi vastaa pelin
pyörimisestä. play_game-metodissa suoritetaan Humanplayer-luokan do_turns-, ask_place_ ja do_turn 
-metodit, joissa kysytään, minne pelaaja haluaa merkin asettaa ja jos asetus on validi, suoritetaan
merkin asetus. Asetuksen validius tarkistetaan Board-luokan check_place_free -metodilla ja 
merkin asetus set_mark -metodilla. Tämän jälkeen vuoro vaihtuu ja sama toistuu. Jokaisen
vuoron jälkeen Game-luokassa tarkastetaan game_is_finished -metodilla, jatkuuko peli vielä vai
onko jompikumpi pelaaja voittanut tai peli päättynyt tasapeliin. 
 
