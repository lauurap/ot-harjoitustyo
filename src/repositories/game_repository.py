class GameRepository:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def store(self, numbers, turn):
        file = open("stored_games.txt", "w")
        board = ""
        for i in range(10):
            board += str(numbers[i])
        file.write(self.name1 + "\n")
        file.write(self.name2 + "\n")
        file.write(board + "\n")
        file.write(str(turn))
        file.close()
        print("Tallennus onnistui")

    def read(self):
        file = open("stored_games.txt", "r")
        name1 = file.readline().strip()
        name2 = file.readline().strip()
        board = file.readline().strip()
        turn = file.readline().strip()
        file.close()
        return [name1, name2, board, turn]
