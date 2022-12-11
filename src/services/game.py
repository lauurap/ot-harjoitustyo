from services.board import Board
from services.humanplayer import HumanPlayer
from services.computerplayer import ComputerPlayer


class Game:
    def __init__(self, name1, name2, turn, numberlist):
        self.board = Board(name1, name2, numberlist)
        self.player1 = HumanPlayer(name1, 'X')
        if name2 == "Kone":
            self.player2 = ComputerPlayer(name2, 'O')
        else:
            self.player2 = HumanPlayer(name2, 'O')
        self.turn = int(turn)

    def play_game(self):
        while self.game_is_finished(self.turn, self.board) is False:
            if self.turn == 1:
                self.player1.do_turns(self.board, self.turn)
                self.turn = 2
                self.board.print_board()
            if self.game_is_finished(self.turn, self.board) is True:
                break
            if isinstance(self.player2, ComputerPlayer) is True:
                self.player2.do_turn(self.board)
                print("Kone on pelannut seuraavasti:")
                self.turn = 1
            else:
                self.player2.do_turns(self.board, self.turn)
                self.turn = 1
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
