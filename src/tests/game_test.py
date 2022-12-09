import unittest
from services.game import Game
from services.board import Board
from services.humanplayer import HumanPlayer


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("Matti", "Maija")
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player1 = HumanPlayer("Matti", 'X')
        self.player2 = HumanPlayer("Maija", 'O')

    def test_game_is_not_finished_return_true_if_full(self):
        for i in range(1, 10):
            self.board.set_mark('X', i)
        self.assertEqual(self.game.game_is_finished(1, self.board), True)

    def test_game_is_not_finished_return_true_if_player1_win(self):
        self.board.set_mark('X', 3)
        self.board.set_mark('X', 6)
        self.board.set_mark('X', 9)
        self.assertEqual(self.game.game_is_finished(1, self.board), True)
