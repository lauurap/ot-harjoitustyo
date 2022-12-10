class HumanPlayer:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def do_turn(self, board, place):
        success = board.set_mark(self.mark, place)
        return success

    def ask_place(self, board, turn):
        correct_place = False
        while correct_place is False:
            place = input("Mihin paikkaan haluat asettaa merkkisi? \n")
            correct_place = board.check_place_free(place, turn)
        return int(place)

    def do_turns(self, board, turn):
        print("Vuorossa on", self.name)
        place = self.ask_place(board, turn)
        while self.do_turn(board, place) is False:
            print("Vuorossa on", self.name)
