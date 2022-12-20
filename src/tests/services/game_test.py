import unittest
from services.game import Game
from services.board import Board
from services.humanplayer import HumanPlayer
from services.computerplayer import ComputerPlayer


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("Matti", "Maija", '1', "123456789")

    def test_game_create_compyterplayer_if_name_is_kone(self):
        self.game = Game("Matti", "Kone", '1', "123456789")
        self.assertEqual(isinstance(self.game.player2, ComputerPlayer), True)

    def test_game_is_not_finished_return_true_if_full(self):
        for i in range(1, 10):
            self.game.board.set_mark('X', i)
        self.assertEqual(self.game.game_is_finished(1, self.game.board), True)

    def test_game_is_not_finished_return_true_if_player1_win(self):
        self.game.board.set_mark('X', 3)
        self.game.board.set_mark('X', 6)
        self.game.board.set_mark('X', 9)
        self.assertEqual(self.game.game_is_finished(2, self.game.board), True)

    def test_game_is_not_finished_return_true_if_player2_win(self):
        self.game.board.set_mark('X', 3)
        self.game.board.set_mark('X', 6)
        self.game.board.set_mark('X', 9)
        self.assertEqual(self.game.game_is_finished(1, self.game.board), True)

    def test_game_is_not_finished_return_true_if_board_full(self):
        self.game = Game("Matti", "Kone", '1', "XOXXXOOXO")
        self.assertEqual(self.game.game_is_finished(1, self.game.board), True)

    def test_game_is_not_finished_return_false_if_not_finished(self):
        self.assertEqual(self.game.game_is_finished(1, self.game.board), False)
