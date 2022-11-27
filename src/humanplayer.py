from board import Board


class Humanplayer:
	def __init__(self, name, mark):
		self.name=name
		self.mark=mark

	def make_move(self,game):
		board = game.give_board()
		place = int(input("Mihin paikkaan haluat merkin asettaa? \n"))
		mark = input("Anna asetettava merkki: \n")
		self.board.set_mark(mark,place)

	#def give_name(self):
		#return name

	#def give_mark(self):
		#return mark