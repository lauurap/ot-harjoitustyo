from services.game import Game
from repositories.game_repository import GameRepository


class TicTacToe:
    """Sovelluksen käynnistämisesta ja käyttöliittymästä vastaava luokka"""

    def __init__(self):
        """Luokan konstruktori"""

        pass

    def create_game(self) -> None:
        """Näyttää aloitusvalikon"""

        COMMANDS = {
            "l": "l Lopeta",
            "a": "a Aloita uusi peli",
            "j": "j Jatka aiempaa peliä",
        }
        menu = "a: Aloita uusi peli \nj: Jatka aiempaa peliä \nl: Lopeta peli \n"
        print("Tervetuloa pelaamaan ristinollaa! \n \n")
        print(menu)
        started = False
        while started is False:
            command = input("Anna komento: \n")
            if not command in COMMANDS:
                print("Anna jokin seuraavista komennoista: \n")
                print(menu)
            if command == "l":
                break
            if command == "a":
                self.start_game()
                started = True
            elif command == "j":
                self.continue_game()
                started = True

    def continue_game(self) -> None:
        """Lukee tiedostosta tallennetun pelin tiedot ja aloittaa uuden pelin kyseisillä tiedoilla"""

        game_repository = GameRepository(" ", " ")
        list = game_repository.read()
        name1 = list[0]
        name2 = list[1]
        numberstring = list[2]
        turn = list[3]
        if name1 not in " ":
            game = Game(name1, name2, turn, numberstring)
            print("\nJatketaan tallennettua peliä!\n")
            game.play_game()
        else:
            print("Ei tallennettua peliä")

    def start_game(self) -> None:
        """Aloittaa uuden pelin"""

        create_name = False
        while create_name is False:
            name1 = input("Anna pelaajan 1 nimi ")
            if name1 in ('', ' '):
                print("Nimessä pitää olla ainakin yksi merkki!")
            else:
                create_name = True
        other_player = False
        while other_player is False:
            response = input("Pelaatko konetta vastaan? ei/kyllä ")
            if response not in ("kyllä", "ei"):
                print("Kirjoita joko ei tai kyllä")
            if response == "ei":
                create_name2 = False
                while create_name2 is False:
                    name2 = input("Anna pelaajan 2 nimi ")
                    if name2 in ('', ' ', name1):
                        print(
                            "Nimi ei saa olla tyhjä eikä se saa olla sama kuin toisen pelaajan nimi!")
                    else:
                        create_name2 = True
                print("Tervetuloa pelaamaan",
                      name1, "ja", name2, "!\n")
                other_player = True
            if response == "kyllä":
                name2 = "Kone"
                other_player = True
        game = Game(name1, name2, "1", "123456789")
        print("\nAloitetaan uusi peli! \n")
        print("Kun ohjelma kysyy merkin paikkaa, voit myös syöttää seuraavan komennon: \nt: Tallenna\n")
        game.play_game()
