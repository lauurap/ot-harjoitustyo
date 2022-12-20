from services.game import Game
from repositories.game_repository import GameRepository


class TicTacToe:
    def __init__(self):
        pass

    def create_game(self) -> None:
        COMMANDS = {
            "l": "l Lopeta",
            "a": "a Aloita uusi peli",
            "j": "j Jatka aiempaa peliä",
        }
        MENU = "a: Aloita uusi peli \nj: Jatka aiempaa peliä \nl: Lopeta peli \n"
        print("Tervetuloa pelaamaan ristinollaa! \n \n")
        print(MENU)
        started = False
        while started is False:
            command = input("Anna komento: \n")
            if not command in COMMANDS:
                print("Anna jokin seuraavista komennoista: \n")
                print(MENU)
            if command == "l":
                break
            if command == "a":
                self.start_game()
                started = True
            elif command == "j":
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
                    started = True
                else:
                    print("Ei tallennettua peliä")

    def start_game(self) -> None:
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
