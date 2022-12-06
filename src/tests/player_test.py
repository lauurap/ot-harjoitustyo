import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_set_players_name_correct(self):
        player = Player("Matti", "X")
        self.assertEqual(player.name, "Matti")

    def test_constructor_set_players_mark_correct(self):
        player = Player("Matti", "X")
        self.assertEqual(player.mark, "X")