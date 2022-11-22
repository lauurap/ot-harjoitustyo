import unittest
from game import Game
from player import Player

class TestGame(unittest.TestCase):
	def setUp(self):
		print("Set up goes here")

	def test_constructor_set_name_correct(self):
		player=Player("Matti")
		self.assertEqual(player.name, "Matti")
		

	def test_players_cant_have_same_name(self): #tarkista onko järkeä
		player1=Player("Hello")
		player2=Player("Hello")
		self.assertEqual(player1.name, player2.name)

	#def test_player_must_have_name(self): #tarkista onko järkeä
	#	player=Player("")
	#	self.assertEqual(player.name, "Nimessä pitää olla ainakin yksi merkki!")