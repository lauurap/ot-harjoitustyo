import unittest
from services.computerplayer import ComputerPlayer
from services.board import Board


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board("Matti", "Maija")
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.computerplayer = ComputerPlayer("Kone", 'X')

    def test_constructor_do_turn_correct(self):
        self.assertEqual(self.computerplayer.do_turn(self.board), True)
