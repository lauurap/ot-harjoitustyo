from repositories.game_repository import GameRepository


class Board:
    """Luokka, joka ylläpitää ristinolla-pelin pelilautaa.

    Attributes:
        name1: Pelaajan 1 nimi
        name2: Pelaajan 2 nimi
        numbersting: Laudalla alkutilanteessa olevat numerot/merkit
    """

    def __init__(self, name1, name2, number_string):
        """Luokan konstruktori, joka luo uuden laudan pelin
        alussa tai jatkettaessa tallennettua peliä.

        Args:
                numbers: Laudalla alussa olevat numerot/merkit listana
                name1: Pelaajan 1 nimi
                name2: Pelaajan 2 nimi
        """

        self.numbers = self.number_string_to_numbers(number_string)
        print("Tässä on pelilauta: \n")
        self.print_board()
        self.name1 = name1
        self.name2 = name2

    def number_string_to_numbers(self, number_string) -> list:
        """Muuttaa laudalla olevat numerot/merkit
        string-muodosta listaksi.

        Args:
                number_string: Laudalla alussa olevat
                numerot/merkit string-muodossa.

        Returns:
                numbers: Laudalla alussa olevat numerot/merkit listana.
        """

        numbers = [" "]
        for i in range(9):
            numbers.append(number_string[i])
        return numbers

    def print_board(self) -> None:
        """Tulostaa pelilaudan.
        """

        print(" ", self.numbers[1], "|", self.numbers[2], "|", self.numbers[3])
        print("-----------")
        print(" ", self.numbers[4], "|", self.numbers[5], "|", self.numbers[6])
        print("-----------")
        print(" ", self.numbers[7], "|", self.numbers[8], "|", self.numbers[9])
        print(" ")

    def check_place_free(self, place, turn) -> bool:
        """Tarkistaa, onko paikka kelvollinen.

        Jos paikaksi annetaan t, ohjelma suorittaa tallennuksen.

        Jos paikka on kelvollinen, tarkistaa onko kyseisellä paikalla
        jo merkki.

        Returns:
                True, jos paikka on kelvollinen ja paikalla ei vielä
                ole merkkiä, muussa tapauksessa False.
        """

        if place == "t":
            game_repository = GameRepository(self.name1, self.name2)
            game_repository.store(self.numbers, turn)
            return False
        try:
            place = int(place)
        except ValueError:
            print("Merkin tulee olla numero!")
            return False
        if int(place) < 1 or int(place) > 9:
            print("Merkki tulee asettaa johonkin ruuduista 1-9!")
            return False
        if self.numbers[int(place)] == 'X' or self.numbers[int(place)] == 'O':
            print("Merkki tulee asettaa vapaalle ruudulle!")
            return False
        return True

    def set_mark(self, mark, place) -> bool:
        """Asettaa pelaajan merkin pelilaudalle pelaajan haluamaan paikkaan

        Returns:
                True, jos asetus on mahdollinen eli paikalla ei vielä ole
                merkkiä, muussa tapauksessa False.
        """

        if self.numbers[place] != 'O' and self.numbers[place] != 'X':
            self.numbers[place] = mark
            return True
        return False

    def check_win(self) -> bool:
        """Tarkastaa, onko laudalla kolme samaa merkkiä vaaka-,
        pysty- tai diagonaalisessa suunnassa.

        Returns:
                True, jos laudalla on kolme samaa merkkiä vaaka-,
                pysty- tai diagonaalisessa suunnassa, muutoin False.
        """

        for i in range(3):
            if self.numbers[i*3+1] == self.numbers[i*3+2] == self.numbers[i*3+3]:
                return True
            if self.numbers[i+1] == self.numbers[i+1+3] == self.numbers[i+1+6]:
                return True
        if self.numbers[1] == self.numbers[5] == self.numbers[9]:
            return True
        if self.numbers[3] == self.numbers[5] == self.numbers[7]:
            return True
        return False

    def check_full(self) -> bool:
        """Tarkastaa, onko laudalla jokaisessa paikassa X tai O.

        Return:
                True, jos laudalla on jokaisessa paikassa X tai O.
                Muussa tapauksessa False.
        """

        marks = 0
        for i in range(10):
            if self.numbers[i] == 'O' or self.numbers[i] == 'X':
                marks += 1
        if marks == 9:
            return True
        return False
