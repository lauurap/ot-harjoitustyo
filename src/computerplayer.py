from player import Player
import random

class Computerplayer(Player):
    def __init__(self, name, mark):
        super().__init__(name, mark)


    def do_turn(self, board):
        success = False
        while success is False:
            place = random.randint(1,9)
            success = board.set_mark(self.mark, place)
        return success