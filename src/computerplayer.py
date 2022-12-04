import random

class Computerplayer:
    def __init__(self, mark):
        self.mark = mark

    def do_turn(self):
        success = False
        while success is False:
            place = random.randint(1,9)
            if self.numbers[place] == 'X' or self.numbers[place] == 'O':
                break

            if self.numbers[place] != 'O' and self.numbers[place] != 'X':
                self.numbers[place] = mark
                success = True

        return success
        