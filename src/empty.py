from repositories.game_repository import GameRepository


def empty():
    game_repository = GameRepository(" ", " ")
    game_repository.store(" 123456789", " ")


if __name__ == "__main__":
    empty()
