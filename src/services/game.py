from services.board import Board
from services.humanplayer import Humanplayer
from services.computerplayer import Computerplayer


class Game:
    def __init__(self, name1, name2):
        print("\nAloitetaan uusi peli! \n")
        self.board = Board()
        self.player1 = Humanplayer(name1, 'X')
        if name2 == "Kone":
            self.player2 = Computerplayer(name2, 'O')
        else:
            self.player2 = Humanplayer(name2, 'O')

    def play_game(self):
        print("Aloitetaan pelaaminen! \n")
        turn = 1
        while self.game_is_finished(turn, self.board) is False:
            self.player1.do_turns(self.board)
            turn = 2
            self.board.print_board()
            if self.game_is_finished(turn, self.board) is True:
                break
            if isinstance(self.player2, Computerplayer) is True:
                self.player2.do_turn(self.board)
                print("Kone on pelannut seuraavasti:")
                turn = 1
            else:
                self.player2.do_turns(self.board)
                turn = 1
            self.board.print_board()

    def game_is_finished(self, turn, board):
        finished = False
        if board.check_win() is True and turn == 2:
            print("Peli loppui!", self.player1.name, "voitti! \n")
            finished = True
            return finished
        if board.check_win() is True and turn == 1:
            print("Peli loppui!", self.player2.name, "voitti! \n")
            finished = True
            return finished
        if board.check_full() is True and board.check_win() is False:
            print("Peli loppui! Tasapeli!")
            finished = True
            return finished
        return finished
