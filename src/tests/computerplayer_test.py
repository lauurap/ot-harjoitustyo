import unittest
from computerplayer import Computerplayer
from board import Board


class TestComputerplayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.computerplayer = Computerplayer("Kone", 'X')

    def test_constructor_do_turn_correct(self):
        self.assertEqual(self.computerplayer.do_turn(self.board), True)
