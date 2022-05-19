from tutorial import Tutorial
from game import Game

class Main():
    def __init__(self) -> None:
        tutorial = Tutorial()
        game = Game()
        game.level_loop()


if __name__ == "__main__":
    text_adventure = Main()