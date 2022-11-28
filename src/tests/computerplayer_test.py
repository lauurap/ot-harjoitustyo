import unittest
from computerplayer import Computerplayer

class TestComputerplayer(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_set_mark_correct(self):
        computerplayer = Computerplayer("X")
        self.assertEqual(computerplayer.mark, "X")