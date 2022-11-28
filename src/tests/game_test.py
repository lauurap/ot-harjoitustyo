import unittest
from game import Game
from humanplayer import Humanplayer


class TestGame(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")


    def test_players_cant_have_same_name(self):  # tarkista onko järkeä
        player1 = Player("Hello", "X")
        player2 = Player("Hello", "O")
        self.assertEqual(player1.name, player2.name)

