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
	


