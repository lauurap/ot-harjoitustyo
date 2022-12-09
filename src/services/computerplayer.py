import random

class ComputerPlayer:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def do_turn(self, board):
        success = False
        while success is False:
            place = random.randint(1, 9)
            success = board.set_mark(self.mark, place)
        return success
