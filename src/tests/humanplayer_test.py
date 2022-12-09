import unittest
from services.humanplayer import Humanplayer
from services.board import Board


class TestHumanplayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.humanplayer = Humanplayer("Matti", 'X')

    def test_constructor_set_name_correct(self):
        humanplayer = Humanplayer("Matti", "X")
        self.assertEqual(humanplayer.name, "Matti")

    def test_constructor_set_mark_correct(self):
        humanplayer = Humanplayer("Matti", "X")
        self.assertEqual(humanplayer.mark, "X")

    def test_constructor_do_turn_correct(self):

        self.assertEqual(self.humanplayer.do_turn(self.board, 1), True)
