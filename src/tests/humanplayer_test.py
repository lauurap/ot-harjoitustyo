import unittest
from humanplayer import Humanplayer
from board import Board


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

    #def test_constructor_do_turn_correct(self):
        #self.humanplayer.input = lambda: '1'
        #output = self.humanplayer.do_turn(self.board)
        #self.assertEqual(output, True)


    #def test_constructor_do_turn_correct(monkeypatch):
        #monkeypatch.setattr('sys.stdin', '1')
        #assert self.humanplayer.do_turn(self.board) == True
