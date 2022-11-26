

class Board:

	def __init__(self):
		self.numbers = [" ",1,2,3,4,5,6,7,8,9]
		print("Tässä on pelilauta: \n")
		self.print_board()

	def print_board(self): #taulun printtaus otettu https://www.youtube.com/watch?v=7Djh-Cbgi0E
		print(" %s | %s | %s " %(self.numbers[1], self.numbers[2], self.numbers[3]))
		print("-----------")
		print(" %s | %s | %s " %(self.numbers[4], self.numbers[5], self.numbers[6]))
		print("-----------")
		print(" %s | %s | %s " %(self.numbers[7], self.numbers[8], self.numbers[9]))
		print(" ")
	def set_mark(self,mark, place):
		success = False
		while success == False:
			if place<1 or place>9:
				print("Merkki tulee asettaa johonkin ruuduista 1-9!")
			else:
				success2 = False
				while success2 == False:
					if self.numbers[place]=='X' or self.numbers[place]=='O':
						print("Merkki tulee asetta vapaalle ruudulle!")
						success2=True

					if self.numbers[place]!='O' and self.numbers[place]!='X':
						self.numbers[place]=mark
							
						success2 = True
						break
			success = True
						

	
	#def check_win(self):
		

	def check_board_full(self):
		marks = 0
		status = False
		for i in range(10):
			if self.numbers[i]=='O' or self.numbers[i]=='X':
				marks+=1
		if marks==9:
			print("Peli loppui! Tasapeli!")
			status = True
		return status
			


