class GameRepository:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def store(self, numbers, turn):
        file = open("stored_games.txt", "w")
        board = ""
        for i in range(10):
            board += str(numbers[i])
        file.write("Pelaaja1, Pelaaja2, lauta, vuoro:")
        file.write(self.name1 + self.name2 + board + str(turn))
        file.close()
        print("Tallennus onnistui")

    def read(self):
        file = open("stored_games.txt", "r")
        stored_boards = file.readlines()
        file.close()
        for line in stored_boards:
            print(line)
