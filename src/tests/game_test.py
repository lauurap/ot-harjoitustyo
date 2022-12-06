import unittest
from game import Game
from board import Board
from humanplayer import Humanplayer


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player1 = Humanplayer("Matti", "X")
        self.player2 = Humanplayer("Maija", "O")

    #def test_board_full_prints_correct(self): 
        #self.player1 = Humanplayer("Matti", "X")
        #self.player2 = Humanplayer("Maija", "O") 
        #for i in range(1, 10):
        #    self.board.set_mark('X', i)
        #output = self.game.play_game()
        #self.assertEqual(output, "Peli loppui! Tasapeli!")
