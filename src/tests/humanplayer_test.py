import unittest
from services.humanplayer import HumanPlayer
from services.board import Board


class TestHumanplayer(unittest.TestCase):
    def setUp(self):
        self.board = Board("Matti", "Maija", "123456789")
        self.humanplayer = HumanPlayer("Matti", 'X')

    def test_constructor_set_name_correct(self):
        self.assertEqual(self.humanplayer.name, "Matti")

    def test_constructor_do_turn_correct(self):
        self.assertEqual(self.humanplayer.do_turn(self.board, 1), True)

    def test_constructor_do_turn_returns_false_if_place_not_correct(self):
        self.board.set_mark('X', 1)
        self.assertEqual(self.humanplayer.do_turn(self.board, 1), False)
