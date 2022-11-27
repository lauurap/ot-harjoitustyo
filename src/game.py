from board import Board
from humanplayer import Humanplayer


class Game:

    def __init__(self):
        print("\nAloitetaan uusi peli! \n")
        self.board = Board()

    def start_game(self):
        createname = True
        while createname is True:
            name1 = input("Anna pelaajan 1 nimi ")
            if name1 in ('', ' '):
                print("Nimessä pitää olla ainakin yksi merkki!")
            else:
                createname = False
        createname2 = True
        while createname2 is True:
            name2 = input("Anna pelaajan 2 nimi ")
            if name2 in ('', ' ', name1):
                print(
                    "Nimi ei saa olla tyhjä eikä se saa olla sama kuin toisen pelaajan nimi!")
            else:
                createname2 = False
        print("Tervetuloa pelaamaan", name1, "ja", name2, "!\n")
        self.player1 = Humanplayer(name1, 'X')
        self.player2 = Humanplayer(name2, 'O')
        #board = Board()

    def play_game(self):
        print("Aloitetaan pelaaminen! \n")
        vuoro = 1
        while self.board.check_board_full() is False and self.board.check_win() is False:
            while vuoro == 1 and self.board.check_board_full() is False and self.board.check_win() is False:
                print("Vuorossa on", self.player1.name,
                      "\n Aseta merkkisi", self.player1.mark, "ruutuun 1-9\n ")
                place = int(input("Mihin paikkaan haluat merkin asettaa? \n"))
                if self.board.set_mark(self.player1.mark, place) is True:
                    vuoro = 2
                self.board.print_board()

            while vuoro == 2 and self.board.check_board_full() is False and self.board.check_win() is False:
                print("Vuorossa on", self.player2.name,
                      "\n Aseta merkkisi", self.player2.mark, "ruutuun 1-9\n ")
                place = int(input("Mihin paikkaan haluat merkin asettaa? \n"))
                if self.board.set_mark(self.player2.mark, place) is True:
                    vuoro = 1
                self.board.print_board()
        if self.board.check_board_full() is True:
            print("Peli loppui! Tasapeli!")
        if self.board.check_win() is True and vuoro == 2:
            print("Peli loppui!", self.player1.name, "voitti! Onnea!\n")
        if self.board.check_win() is True and vuoro == 1:
            print("Peli loppui!", self.player2.name, "voitti! Onnea!\n")
