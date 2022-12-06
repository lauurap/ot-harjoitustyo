from player import Player

class Humanplayer(Player):
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark

    def do_turn(self, board):
        success = False
        text = "Mihin paikkaan haluat asettaa merkkisi? \n"
        print("Vuorossa on", self.name, "\nAseta merkkisi", self.mark)
        try:
            place = int(input(text))
        except ValueError:
            print("Merkin tulee olla numero!")
            return success
        if int(place) < 1 or int(place) > 9:
            print("Merkki tulee asettaa johonkin ruuduista 1-9!")
            return success
        if board.set_mark(self.mark, int(place)) is False:
            print("Merkki tulee asettaa vapaalle ruudulle!")
            return success
        if board.set_mark(self.mark, int(place)) is True:
            board.set_mark(self.mark, int(place))
            success = True
            return success
