from game import Game
from board import Board

COMMANDS = {
	"q": "q Lopeta",
	"a": "a Aloita uusi peli",
	"j": "j Jatka aiempaa peliä",
}

def main():
	print("Tervetuloa pelaamaan ristinollaa! \n \n Aloita uusi peli kirjoittamalla a \n Jatka aiempaa peliä kirjoittamalla j \n Lopeta peli painamalla q \n")
	started = False
	while started==False:
		command = input("Anna komento: \n")

		if not command in COMMANDS:
			print("Virheellinen komento. \n Aloita uusi peli kirjoittamalla a \n Jatka aiempaa peliä kirjoittamalla j \n Lopeta peli painamalla q \n")
			continue
		if command == "q":
			print("Sorry, ei vielä valmis, joten peli loppuu ilman tallennusmahdollisuutta")
			#kysy tallennusta tai tallenna peli
			break
		elif command == "a":
			#board = Board()
			
			game = Game()
			game.start_game()
			#board.set_mark('X',1)
			game.play_game()
			#board.print_board()
			started=True
		elif command == "j":
			print("Sorry, ei vielä vamis")
			#self.continue_game()


if __name__ == "__main__":
    main()
