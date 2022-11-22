from board import Board
from player import Player

class Game:

	def __init__(self):
		print("\nAloitetaan uusi peli! \n")	
		#self.board = Board()
		

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
		self.player1 = Player(name1)
		self.player2 = Player(name2)
		board = Board()
		

	def play_game(self):
		#joku while tähän
		print("Aloitetaan pelaaminen! Mutta ehkä vasta ensi viikolla...")
		#self.player1.set_mark(board)
		