class GameRepository:
    """Luokka, jonka avulla tallennetaan peli ja luetaan tallennettu peli.

    Attributes:
        name1 = Pelaajan 1 nimi
        name2 = Pelaajan 2 nimi
    """

    def __init__(self, name1, name2):
        """Luokan konstruktori, joka luo uuden GameRepository-olion.

        Args:
            name1 = Pelaajan 1 nimi
            name2 = Pelaajan 2 nimi
        """

        self.name1 = name1
        self.name2 = name2

    def store(self, numbers, turn) -> None:
        """Tallentaa pelaajat, pelilaudan ja seuraavana vuorossa olevan pelaajan vuoron.
        """

        with open("src/stored_games.txt", "w", encoding='UTF-8') as file:
            board = ""
            for i in range(10):
                board += str(numbers[i])
            file.write(self.name1 + "\n")
            file.write(self.name2 + "\n")
            file.write(board + "\n")
            file.write(str(turn))

    def read(self) -> list:
        """Lukee tiedostosta tallenetun pelin palaajat, pelilaudan
        ja seuraavana vuorossa olevan pelaajan vuoron.

        Returns:
            Listan, jossa on pelaajien nimet, pelilauta ja pelivuoro.
        """

        with open("src/stored_games.txt", "r", encoding='UTF-8') as file:
            name1 = file.readline().strip()
            name2 = file.readline().strip()
            board = file.readline().strip()
            turn = file.readline().strip()
        return [name1, name2, board, turn]
