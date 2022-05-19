from time import sleep


class Tutorial():
    def __init__(self) -> None:
        self.explanation()

    def explanation(self) -> None:
        user_input = input("Skip Tutorial[Y/N]:\n$  ~  ")
        if user_input == "N":
            print("Welcome to this Text Adventure")
            sleep(1)
            print("You have to go through 10 Level")
            print("You can go to the next level, by finding and going through the door")
            sleep(3)
            print("But watch out, there will be MOBS and their trying to stop and kill you")
            print("But there are also other things like Traps or Walls which can kill or block your way")
            sleep(8)
            print("But on your way, there are also items, which can help you")
            print("The game starts now, you can time the commands now, if you don`t know them, just typ help\n\n")
            sleep(10)