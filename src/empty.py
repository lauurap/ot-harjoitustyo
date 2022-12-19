from repositories.game_repository import GameRepository


def build():
    game_repository = GameRepository(" ", " ")
    game_repository.store(" 123456789", "1")


if __name__ == "__main__":
    build()
