from player import Player

class Humanplayer(Player):
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark

    def do_turn(self, board):
        success = False
        text = "Mihin paikkaan haluat asettaa merkkisi? \n"
        print("Vuorossa on", self.name, "\nAseta merkkisi", self.mark)
        place = int(input(text))
        while success is False:
            if place < 1 or place > 9:
                print("Merkki tulee asettaa johonkin ruuduista 1-9!")
                break
            #if board.set_mark(self.mark, place) is False:
                #print("Merkki tulee asettaa vapaalle ruudulle!")
                #break
            success = board.set_mark(self.mark, place)
        return success
