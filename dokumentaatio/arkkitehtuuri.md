# Arkkitehtuuri

## Rakenne

Koodin pakkausrakenne on alla: 

![](./kuvat/pakkausrakenne1.PNG)

Pakkaus ui sisältää käyttöliittymän koodin ja services sisältää sovelluslogiikan koodin, eli luokat Game, Board, 
Humanplayer ja Computerplayer. Repositories vastaa tietojen tallentamisen tiedostoon ja tietojen lukemisen tiedostosta.

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
          numberstring_to_numbers()
          print_board()
          check_place_free()
          set_mark()
          check_win()
          check_board_full()

      }
      class Game{
          name1
          name2
          turn
          numberstring
          play_game()
          game_is_finished()
      }
      class Humanplayer{
          name
          mark
          do_turn()
      }
      class Computerplayer{
          name
          mark
          do_turn()
          ask_place()
          do_turns()
      }
      class Player{
          name
          mark
          do_turn()
      }
```

## Pelin tallennus

Pakkauksen repositories luokka GameRepository vastaa pelin tallentamisesta. GameRepositoryn metodi store tallentaa pelin
pelaajat, vuorossa olevan pelaajan ja pelilaudan tiedostoon. GameRepositoryn metodi read lukee tiedostosta vastaavat tiedot. 

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