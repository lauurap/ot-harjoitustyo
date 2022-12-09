from services.game import Game

class Tictactoe:

    def __init__(self):
        pass

    def jotain(self):
        COMMANDS = {
            "q": "q Lopeta",
            "a": "a Aloita uusi peli",
            "j": "j Jatka aiempaa peliä",
        }
        MENU = "a: Aloita uusi peli \nj: Jatka aiempaa peliä \nq: Lopeta peli \n"
        print("Tervetuloa pelaamaan ristinollaa! \n \n")
        print(MENU)
        started = False
        while started is False:
            command = input("Anna komento: \n")
            if not command in COMMANDS:
                print("Anna jokin seuraavista komennoista: \n")
                print(MENU)
            if command == "q":
                print(
                    "Sorry, ei vielä valmis, joten peli loppuu ilman tallennusmahdollisuutta")
                started = True
                break
            if command == "a":
                self.create_game()
                started = True
            elif command == "j":
                print("Sorry, ei vielä vamis")

    def create_game(self):
        createname = False
        while createname is False:
            name1 = input("Anna pelaajan 1 nimi ")
            if name1 in ('', ' '):
                print("Nimessä pitää olla ainakin yksi merkki!")
            else:
                createname = True
        response = input("Pelaatko konetta vastaan? ei/kyllä ")
        if response == "ei":
            createname2 = False
            while createname2 is False:
                name2 = input("Anna pelaajan 2 nimi ")
                if name2 in ('', ' ', name1):
                    print(
                        "Nimi ei saa olla tyhjä eikä se saa olla sama kuin toisen pelaajan nimi!")
                else:
                    createname2 = True
                print("Tervetuloa pelaamaan",
                      name1, "ja", name2, "!\n")
        if response == "kyllä":
            name2 = "Kone"
        game = Game(name1, name2)
        game.play_game()
