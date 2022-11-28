import unittest
from humanplayer import Humanplayer

class TestHumanplayer(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_set_name_correct(self):
        humanplayer = Humanplayer("Matti", "X")
        self.assertEqual(humanplayer.name, "Matti")

    def test_constructor_set_mark_correct(self):
        humanplayer = Humanplayer("Matti", "X")
        self.assertEqual(humanplayer.mark, "X")