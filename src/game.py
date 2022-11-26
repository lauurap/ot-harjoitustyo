from board import Board
from player import Player
from humanplayer import Humanplayer

class Game:

	def __init__(self):
		print("\nAloitetaan uusi peli! \n")	
		self.board = Board()

		

	def start_game(self):
		createname = True
		while createname == True:		
			name1 = input("Anna pelaajan 1 nimi ")
			if name1==" " or name1=="":
				print("Nimessä pitää olla ainakin yksi merkki!")
			else:
				createname=False
		createname2 = True
		while createname2 == True:
			name2 = input("Anna pelaajan 2 nimi ")
			if name2==" " or name2=="" or name1==name2:
				print("Nimessä pitää olla ainakin yksi merkki eikä se saa olla sama kuin toisen pelaajan nimi!")
			else:
				createname2=False
		print("Tervetuloa pelaamaan", name1, "ja", name2,"!\n")
		self.player1 = Humanplayer(name1, 'X')
		self.player2 = Humanplayer(name2, 'O')
		#board = Board()
		

	def play_game(self):
		#joku while tähän
		print("Aloitetaan pelaaminen!")
		#win = False
		while self.board.check_board_full() == False:
			mark = input("Anna asetettava merkki: \n")
			place = int(input("Mihin paikkaan haluat merkin asettaa? \n"))
			self.board.set_mark(mark,place)
			#self.player.make_move(game)
			self.board.print_board()
			self.board.check_board_full()

	def give_board():
		return this.board
		