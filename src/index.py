from ui.tictactoe import Tictactoe

COMMANDS = {
    "q": "q Lopeta",
    "a": "a Aloita uusi peli",
    "j": "j Jatka aiempaa peliä",
}
MENU = "a: Aloita uusi peli \nj: Jatka aiempaa peliä \nq: Lopeta peli \n"


def main():
    tictactoe = Tictactoe()
    tictactoe.jotain()


if __name__ == "__main__":
    main()
