import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_created_board_exist(self):
        self.assertNotEqual(self.board, None)

    def test_set_mark(self):
        self.board.set_mark('X', 1)
        self.assertEqual(self.board.numbers[1], 'X')

    def test_constructor_set_mark_correct(self):
        self.assertEqual(self.board.set_mark('X', 7), True)

    def test_constructor_not_set_mark_outside_board(self):
        self.assertEqual(self.board.set_mark('X', 0), False)


    def test_constructor_not_set_mark_same_place(self):
        self.board.set_mark('X', 1)
        self.assertEqual(self.board.set_mark('X', 1), False)

    def test_board_full(self):
        for i in range(1,10):
                self.board.set_mark('X', i)
        self.assertEqual(self.board.check_board_full(), True)

    def test_board_full_if_not_full(self):
        for i in range(1,9):
                self.board.set_mark('X', i)
        self.assertEqual(self.board.check_board_full(), False)
