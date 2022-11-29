import unittest
from game import Game
from board import Board
from humanplayer import Humanplayer


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]


    def test_players_cant_have_same_name(self):  # tarkista onko järkeä
        humanplayer1 = Humanplayer("Hello", "X")
        humanplayer2 = Humanplayer("Hello", "O")
        self.assertEqual(humanplayer1.name, humanplayer2.name)

