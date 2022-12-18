from services.board import Board
from services.humanplayer import HumanPlayer
from services.computerplayer import ComputerPlayer


class Game:
    """Luokka, jonka avulla pelin pelaaminen suoritetaan.

    Attributes:
        name1: Pelaajan 1 nimi
        name2: Pelaajan 2 nimi
        turn: Vuoro, joka määrittää kumpi pelaaja pelaa
        numberstring: Laudalla alkutilanteessa olevat numerot/merkit
    """

    def __init__(self, name1, name2, turn, number_string):
        """Luokan konstruktori, joka luo uuden pelin.

        Args:
            board: Lauta aloitustilanteessa.
            player1: Pelaaja 1 on ihmispelaaja
            player2: Pelaaja 2 on ihmispelaaja tai konepelaaja nimen perusteella
            turn: Vuoro, joka määrittää kumpi pelaaja pelaa
        """

        self.board = Board(name1, name2, number_string)
        self.player1 = HumanPlayer(name1, 'X')
        if name2 == "Kone":
            self.player2 = ComputerPlayer(name2, 'O')
        else:
            self.player2 = HumanPlayer(name2, 'O')
        self.turn = int(turn)

    def play_game(self) -> None:
        """Vastaa pelin pelaamisen suorittamisesta. Kun peli on kesken, vaihtaa
        pelaajan vuoroja ja antaa pelaajalle pelivuoron.
        """

        while self.game_is_finished(self.turn, self.board) is False:
            if self.turn == 1:
                self.player1.do_turns(self.board, self.turn)
                self.turn = 2
                self.board.print_board()
            if self.game_is_finished(self.turn, self.board) is True:
                break
            if isinstance(self.player2, ComputerPlayer) is True:
                self.player2.do_turn(self.board)
                print("Kone on pelannut seuraavasti:")
                self.turn = 1
            else:
                self.player2.do_turns(self.board, self.turn)
                self.turn = 1
            self.board.print_board()

    def game_is_finished(self, turn, board) -> bool:
        """Vastaa pelin tilan tarkistamisesta. Tarkistaa, onko pelissä voittaja tai tasapeli.

        Returns:
            True, jos pelissä jompikumpi pelaaja on voittanut tai
            pelissä on tasapelitilanne, muussa tapauksessa False.
        """

        if board.check_win() is True and turn == 2:
            print("Peli loppui!", self.player1.name, "voitti! \n")
            return True
        if board.check_win() is True and turn == 1:
            print("Peli loppui!", self.player2.name, "voitti! \n")
            return True
        if board.check_full() is True and board.check_win() is False:
            print("Peli loppui! Tasapeli!")
            return True
        return False
