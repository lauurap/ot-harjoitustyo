from board import Board
from humanplayer import Humanplayer
from computerplayer import Computerplayer
from player import Player

class Game:
    def __init__(self):
        print("\nAloitetaan uusi peli! \n")
        self.board = Board()
        self.player1 = Player("name1", 'X')
        self.player2 = Player("name2", 'O')

    def start_game(self):
        createname = False
        while createname is False:
            name1 = input("Anna pelaajan 1 nimi ")
            if name1 in ('', ' '):
                print("Nimessä pitää olla ainakin yksi merkki!")
            else:
                createname = True
                self.player1 = Humanplayer(name1, 'X')
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
                    print("Tervetuloa pelaamaan", name1, "ja", name2, "!\n")
                    self.player2 = Humanplayer(name2, 'O')
        if response == "kyllä":
            self.player2 = Computerplayer("Kone", 'O')

    def play_game(self):
        print("Aloitetaan pelaaminen! \n")
        turn = 1
        while self.board.check_board_full() is False and self.board.check_win() is False:
            if turn == 1:
                turn = 2
                self.player1.do_turn(self.board)
                self.board.print_board()
            if turn == 2 and self.board.check_board_full() is False and self.board.check_win() is False:
                if isinstance(self.player2, Humanplayer) is True:
                    turn = 1
                    self.player2.do_turn(self.board)
                    self.board.print_board()
                else:
                    self.player2.do_turn(self.board)
                    turn = 1
                    print("Kone on pelannut seuraavasti:")
                    self.board.print_board()
        if self.board.check_win() is True and turn == 2:
            print("Peli loppui!", self.player1.name, "voitti! \n")
        if self.board.check_win() is True and turn == 1:
            print("Peli loppui!", self.player2.name, "voitti! \n")
        if self.board.check_board_full() is True and self.board.check_win() is False:
            print("Peli loppui! Tasapeli!")
