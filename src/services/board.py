from repositories.game_repository import GameRepository
#from services.game import Game

class Board:
    def __init__(self,name1,name2):
        self.numbers = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("Tässä on pelilauta: \n")
        self.print_board()
        self.name1 = name1
        self.name2 = name2


    def print_board(self):
        print(" ", self.numbers[1], "|", self.numbers[2], "|", self.numbers[3])
        print("-----------")
        print(" ", self.numbers[4], "|", self.numbers[5], "|", self.numbers[6])
        print("-----------")
        print(" ", self.numbers[7], "|", self.numbers[8], "|", self.numbers[9])
        print(" ")

    def check_place_free(self, place, turn):
        free = False
        if place == "t":
            print("Tallennetaan!")
            game_repository = GameRepository(self.name1, self.name2)
            game_repository.store(self.numbers, turn)
            game_repository.read()
        try:
            place = int(place)
        except ValueError:
            print("Merkin tulee olla numero!")
            return free
        if int(place) < 1 or int(place) > 9:
            print("Merkki tulee asettaa johonkin ruuduista 1-9!")
            return free
        if self.numbers[int(place)] == 'X' or self.numbers[int(place)] == 'O':
            print("Merkki tulee asettaa vapaalle ruudulle!")
            return free
        free = True
        return free

    def set_mark(self, mark, place):
        if self.numbers[place] != 'O' and self.numbers[place] != 'X':
            self.numbers[place] = mark
            return True
        return False

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

    def check_full(self):
        marks = 0
        full = False
        for i in range(10):
            if self.numbers[i] == 'O' or self.numbers[i] == 'X':
                marks += 1
        if marks == 9:
            full = True
        return full
