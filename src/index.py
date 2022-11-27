from game import Game


COMMANDS = {
    "q": "q Lopeta",
    "a": "a Aloita uusi peli",
    "j": "j Jatka aiempaa peliä",
}
MENU = "Aloita uusi peli kirjoittamalla a \nJatka aiempaa peliä kirjoittamalla j \nLopeta peli painamalla q \n"


def main():
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
            # kysy tallennusta tai tallenna peli
            started = True
            break
        if command == "a":
            #board = Board()

            game = Game()
            game.start_game()
            # board.set_mark('X',1)
            game.play_game()
            # board.print_board()
            started = True
        elif command == "j":
            print("Sorry, ei vielä vamis")
            # self.continue_game()


if __name__ == "__main__":
    main()
