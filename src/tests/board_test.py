import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_created_board_exist(self):
        self.assertNotEqual(self.board, None)

    #def test_check_if_board_full(self):
        #self.board.set_mark('X', 7)
        #self.assertEqual(self.numbers[7], 'X')

    def test_constructor_set_mark_correct(self):
        self.assertEqual(self.board.set_mark('X', 7), True)

    def test_constructor_not_set_mark_outside_board(self):
        self.assertEqual(self.board.set_mark('X', 0), False)
