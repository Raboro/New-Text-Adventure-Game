from dataclasses import dataclass, field
from map import MapOne, MapTwo, MapThree, MapFour, MapFive, MapSix, MapSeven, MapEight, MapNine, MapTen
from player import Player
from inventar import Inventar


@dataclass(slots=True)
class Game():
    MAP_SIZE: list = field(init=False)
    MAP_LIST: list = field(init=False)
    COMMANDS: dict = field(init=False)
    MAX_LEVEL: int = 9
    level: int = 0
    next_level: bool = False
    dead: bool = False
    map: object = field(init=False)
    player: object = field(init=False)
    inventar: object = field(init=False)

    

    def __post_init__(self) -> None:
        self.MAP_SIZE = [10, 15, 20, 25, 40, 50, 70, 80, 90, 100]
        self.MAP_LIST = [MapOne, MapTwo, MapThree, MapFour, MapFive, MapSix, MapSeven, MapEight, MapNine, MapTen]
        self.COMMANDS = {
            "help": self.print_commands,
	        "print_map": self.print_map,
            "left": self.left,
            "right": self.right,
            "forward": self.forward,
            "backward": self.backward,
            "print_character_values": self.print_character_values,
            "print_inventar": self.print_inventar,
            "get_item_info": self.get_item_info,
            "use_item": self.use_item
        }


    def create_map(self) -> None:
        self.map = self.MAP_LIST[self.level](SIZE=self.MAP_SIZE[self.level])
        self.map.get_values()


    def level_loop(self) -> None:
        print(f"\n---------Level {self.level+1}---------\n\n")
        self.create_map()
        self.player = Player()
        self.inventar = Inventar()

        while True:
            if self.next_level == True:
                self.next_level = False
                break
            
            elif self.dead == True:
                break

            user_command = input("\nSelect a Command:\n$ ~  ")
            try:
                print("\n")
                self.COMMANDS[user_command]()

            except KeyError:
                print("Please select a correct command\n")

        
        if self.dead == True:
            print("\nYou died :/")
            return

        if self.level == self.MAX_LEVEL:
            print("\nYou are the WINNER")
            return
        else:
            self.level += 1
            self.level_loop()

    
    # Commands
    def print_commands(self) -> None:
        for index, cmd in enumerate(self.COMMANDS):
            if index < 10:
                print(f"{index}  -> {cmd}")
            else:
                print(f"{index} -> {cmd}")

    
    def print_map(self) -> None:
        for row in self.map.player_map:
            print(row)

        for i in self.map.hidden_map:
            print(i)


    def left(self) -> None:
        if self.map.y > 0:  # if player can go there
            result = self.map.check_field(self.map.x, self.map.y-1)

            if result == "next_level":
                self.next_level = True

            elif result == "Dead":
                self.dead = True


    def right(self) -> None:
        if self.map.y < len(self.map.player_map[0]) -1 :  # if player can go there
            result = self.map.check_field(self.map.x, self.map.y+1)

            if result == "next_level":
                self.next_level = True

            elif result == "Dead":
                self.dead = True
            


    def forward(self) -> None:
        if self.map.x > 0:  # if player can go there
            result = self.map.check_field(self.map.x-1, self.map.y)

            if result == "next_level":
                self.next_level = True

            elif result == "Dead":
                self.dead = True
            


    def backward(self) -> None:
        if self.map.x < len(self.map.player_map) - 1:  # if player can go there
            result = self.map.check_field(self.map.x+1, self.map.y)

            if result == "next_level":
                self.next_level = True

            elif result == "Dead":
                self.dead = True
            


    def print_character_values(self) -> None:
        print(f"HP: {self.player.health_points}/{self.player.max_health}\nDamage: {self.player.damage}\nArmor: {self.player.armor}")


    def print_inventar(self) -> None:
        for row in self.inventar.inventar_gui:
            print(row)


    def get_item_info(self) -> None:
        for index, item in enumerate(self.map.ITEMS.items_list):
            if item  in ["S1-", "S2-", "S3-", "S4-", "S5-", "S6-", "S7-", "S8-", "S9-", "S10"]:
                item = "S?-"

            elif item  in ["A1-", "A2-", "A3-", "A4-", "A5-", "A6-", "A7-", "A8-", "A9-", "A10"]:
                item = "A?-"

            print(f"{index}: {self.map.ITEMS.item_description[item]}")


    def use_item(self):
        self.print_inventar()

        item_index = int(input("\nSelect a item, by typing the number:\n$ ~  ")) - 1
        if self.inventar.inventar_elements[item_index] != "---":
            item_to_use = self.inventar.inventar_elements[item_index]
            self.inventar.remove_item(item_index)

            if item_to_use in ["RAA", "RM-", "RD-", "RT-", "RI-", "KAM", "SFM"]:
                self.map.use_item(item=item_to_use)

            else:
                self.player.change_values_by_item(item=item_to_use)
        
        else:
            print("\nWrong input\n")