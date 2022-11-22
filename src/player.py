from board import Board

class Player:
	def __init__(self,name):
		self.name=name

	def set_mark(self,board):
		board.print_board()