import unittest
from repositories.game_repository import GameRepository


class TestGameRepository(unittest.TestCase):
    def setUp(self):
        self.game_repository = GameRepository("Matti", "Maija")
        self.numbers = " 1234567XO"

    def test_read(self):
        self.game_repository.store(self.numbers, 1)
        self.assertEqual(self.game_repository.read(), [
                         "Matti", "Maija", "1234567XO", '1'])
