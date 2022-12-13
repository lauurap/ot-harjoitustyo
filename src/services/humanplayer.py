class HumanPlayer:
    """Luokka, joka tekee ihmispelaajan pelivuoroja

    Attributes:
        name: Ihmispelaajan nimi
        mark: Ihmispelaajan merkki
    """

    def __init__(self, name, mark):
        """Luokan konstruktori, joka luo uuden ihmispelaajan.

        Args:
            name: Ihmispelaajan nimi
            mark: Ihmispelaajan merkki
        """

        self.name = name
        self.mark = mark

    def do_turn(self, board, place):
        """Asettaa merkin pelilaudalle.

        Returns:
            True, jos merkin asetus onnistuu, muussa tapauksessa False.
        """
        success = board.set_mark(self.mark, place)
        return success

    def ask_place(self, board, turn):
        """Kysyy pelaajalta, mihin pelaaja haluaa asettaa merkin.

        Args:
            board: Pelilauta, jonne merkki asetetaan
            turn: Vuorossa olevan pelaajan vuoro

        Returns:
            place eli paikan, jos paikka hyväksytään
        """

        correct_place = False
        while correct_place is False:
            place = input("Mihin paikkaan haluat asettaa merkkisi? \n")
            correct_place = board.check_place_free(place, turn)
        return int(place)

    def do_turns(self, board, turn):
        """Vastaa paikan kysymisestä ja pelivuoron suorittamisesta.
        """

        print("Vuorossa on", self.name)
        place = self.ask_place(board, turn)
        while self.do_turn(board, place) is False:
            print("Vuorossa on", self.name)
