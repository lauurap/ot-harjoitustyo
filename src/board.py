

class Board:

    def __init__(self):
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("Tässä on pelilauta: \n")
        self.print_board()

    def print_board(self):
        print(" ", self.numbers[1], "|", self.numbers[2], "|", self.numbers[3])
        print("-----------")
        print(" ", self.numbers[4], "|", self.numbers[5], "|", self.numbers[6])
        print("-----------")
        print(" ", self.numbers[7], "|", self.numbers[8], "|", self.numbers[9])
        print(" ")

    def set_mark(self, mark, place):
        success = False
        while success is False:
            if place < 1 or place > 9:
                print("Merkki tulee asettaa johonkin ruuduista 1-9!")
                break

            if self.numbers[place] == 'X' or self.numbers[place] == 'O':
                print("Merkki tulee asetta vapaalle ruudulle!")
                break

            if self.numbers[place] != 'O' and self.numbers[place] != 'X':
                self.numbers[place] = mark
                success = True

        return success

    def check_win(self):
        win = False
        for i in range(3):
            if self.numbers[i*3+1] == self.numbers[i*3+2] == self.numbers[i*3+3]:
                win = True
            if self.numbers[i+1] == self.numbers[i+1+3] == self.numbers[i+1+6]:
                win = True
        if self.numbers[1] == self.numbers[5] == self.numbers[9]:
            win = True
        if self.numbers[3] == self.numbers[5] == self.numbers[7]:
            win = True
        return win

    def check_board_full(self):
        marks = 0
        status = False
        for i in range(10):
            if self.numbers[i] == 'O' or self.numbers[i] == 'X':
                marks += 1
        if marks == 9:
            status = True
        return status
