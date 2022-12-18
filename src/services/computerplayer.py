import random


class ComputerPlayer:
    """Luokka, joka tekee tietokonepelaajan pelivuoroja

    Attributes:
        name: Tietokonepelaajan nimi
        mark: Tietokonepelaajan merkki
    """

    def __init__(self, name, mark):
        """Luokan konstruktori, joka luo uuden tietokonepelaajan.

        Args:
            name: Tietokonepelaajan nimi
            mark: Tietokonepelaajan merkki
        """

        self.name = name
        self.mark = mark

    def do_turn(self, board) -> bool:
        """Asettaa merkin pelilaudalle randomilla määriteltyyn paikkaan.

        Args:
            board: Pelilauta, jonne merkki asetetaan

        Returns:
            True, jos merkin asetus onnistuu, muussa tapauksessa False.
        """

        success = False
        while success is False:
            place = random.randint(1, 9)
            success = board.set_mark(self.mark, place)
        return success
