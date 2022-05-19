from dataclasses import dataclass, field
from monster import Alien, Boom, Chief, Kobold, Lellek, Ork, Villain, Zombie
from items import Items
from inventar import Inventar
from player import Player
from random import randint


@dataclass(slots=True)
class Map():
    SIZE: int 
    MOPS_COUNTER: list[int] = field(init=False)
    MOBS: list[str] = field(init=False)
    INTERACTIONS_COUNTER: list[int] = field(init=False)
    INTERACTIONS: list[str] = field(init=False)
    ITEMS: object = field(init=False) 
    START_X: int = 0
    START_Y: int = 0
    x: int = 0
    y: int = 0
    player_map: list[list[str]] = field(init=False)
    hidden_map: list[list[str]] = field(init=False)
    generate_mob: dict[object] = field(init=False)


    def get_valid_pos_to_insert_element_in_hidden_map(self) -> tuple[int, int]:
        while True:
            pos_x = randint(0, self.SIZE - 1) 
            pos_y = randint(0, self.SIZE - 1)

            if self.hidden_map[pos_x][pos_y] == "---":
                return pos_x, pos_y


    def add_element_to_hidden_map(self, elements: list[int], elements_counter: list[int]) -> None:
        for index, element in enumerate(elements):
            for _ in range(elements_counter[index]):
                pos_x, pos_y = self.get_valid_pos_to_insert_element_in_hidden_map()
                
                self.hidden_map[pos_x][pos_y] = element
            

    def create_hidden_map(self, items: list[str], item_counter: list[int]) -> None:
        self.add_element_to_hidden_map(elements=items, elements_counter=item_counter)  # add items
        self.add_element_to_hidden_map(elements=self.MOBS, elements_counter=self.MOPS_COUNTER)  # add MOBS
        self.add_element_to_hidden_map(elements=self.INTERACTIONS, elements_counter=self.INTERACTIONS_COUNTER)  # add INTERACTIONS (wall; trap)
        self.add_element_to_hidden_map(elements=["-D-"], elements_counter=[1])  # add door


    def create_player_map(self) -> None:
        self.player_map = [["---" for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.player_map[self.START_X][self.START_Y] = "-P-"
        self.hidden_map = [["---" for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.hidden_map[self.START_X][self.START_Y] = "-P-"

    
    def check_field(self, x: int, y: int) -> str:
        if self.hidden_map[x][y] == "-|-":  # wall
            return ""
        
        elif self.hidden_map[x][y] == "-D-":  # door
            return "next_level"

        elif self.hidden_map[x][y] == "-T-":  # trap
            return "Dead"

        elif self.hidden_map[x][y] in self.MOBS:  # MOBS
            mob = self.generate_mob[self.hidden_map[x][y]]()
            p = Player()
            fight_result = p.fight(mob)
            if fight_result:
                return "Dead"
        
        elif self.hidden_map[x][y] == "---":  # Nothing
            pass

        else:  # item
            inventar = Inventar()
            inventar.add_item(self.hidden_map[x][y])

        self.hidden_map[self.x][self.y] = "---"
        self.player_map[self.x][self.y] = "---"
        self.x = x
        self.y = y
        self.hidden_map[self.x][self.y] = "-P-"
        self.player_map[self.x][self.y] = "-P-"

        return ""


    def show_requestet_map_character_by_item(self, compare_list: list[str]) -> None:
        for index_col, col in enumerate(self.hidden_map):
                for index_row, row in enumerate(col):
                    if row in compare_list:
                        self.player_map[index_col][index_row] = row
    

    def use_item(self, item: str) -> None:
        if item == "SFM":
            self.player_map = self.hidden_map

        elif item == "KAM":
            self.hidden_map = [[row if row not in self.MOBS else "---" for row in col] for col in self.hidden_map]
        
        elif item == "RAA":
            self.player_map[self.x][self.y-1] = self.hidden_map[self.x][self.y-1]
            self.player_map[self.x][self.y+1] = self.hidden_map[self.x][self.y+1]
            self.player_map[self.x-1][self.y] = self.hidden_map[self.x-1][self.y]
            self.player_map[self.x+1][self.y] = self.hidden_map[self.x+1][self.y]

        elif item == "RM-":
            self.show_requestet_map_character_by_item(compare_list=self.MOBS)
        
        elif item == "RD-":
            self.show_requestet_map_character_by_item(compare_list=["-D-"])
        
        elif item == "RT-":
            self.show_requestet_map_character_by_item(compare_list=["-T-"])

        elif item == "RI-":
            self.show_requestet_map_character_by_item(compare_list=self.ITEMS.items_list)


class MapOne(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [10, 5]
        self.MOBS = ["-O-", "-L-"]
        self.INTERACTIONS_COUNTER = [5, 2]
        self.INTERACTIONS = ["-|-", "-T-"]

        self.ITEMS = Items()
        self.ITEMS.level_one()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek
        }

  

class MapTwo(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [15, 10, 5]
        self.MOBS = ["-O-", "-L-", "-K-"]
        self.INTERACTIONS_COUNTER = [10, 3]
        self.INTERACTIONS = ["-|-", "-T-"]
        
        self.ITEMS = Items()
        self.ITEMS.level_two()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold
        }




class MapThree(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [25, 20, 10]
        self.MOBS = ["-O-", "-L-", "-K-"]
        self.INTERACTIONS_COUNTER = [20, 4]
        self.INTERACTIONS = ["-|-", "-T-"]

        self.ITEMS = Items()
        self.ITEMS.level_three()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold
        }

  

class MapFour(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [20, 10, 10, 5]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-"]
        self.INTERACTIONS_COUNTER = [30, 10]
        self.INTERACTIONS = ["-|-", "-T-"]
        
        self.ITEMS = Items()
        self.ITEMS.level_four()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie
        }



class MapFive(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [20, 20, 20, 20]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-"]
        self.INTERACTIONS_COUNTER = [45, 12]
        self.INTERACTIONS = ["-|-", "-T-"]

        self.ITEMS = Items()
        self.ITEMS.level_five()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie
        }

  

class MapSix(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [50, 40, 40, 40, 20]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-", "-A-"]
        self.INTERACTIONS_COUNTER = [55, 22]
        self.INTERACTIONS = ["-|-", "-T-"]
        
        self.ITEMS = Items()
        self.ITEMS.level_six()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie,
            "-A-": Alien
        }



class MapSeven(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [50, 50, 50, 50, 40]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-", "-A-"]
        self.INTERACTIONS_COUNTER = [75, 32]
        self.INTERACTIONS = ["-|-", "-T-"]

        self.ITEMS = Items()
        self.ITEMS.level_seven()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie,
            "-A-": Alien
        }

  

class MapEight(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [70, 70, 70, 70, 50, 30]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-", "-A-", "-B-"]
        self.INTERACTIONS_COUNTER = [75, 32]
        self.INTERACTIONS = ["-|-", "-T-"]
        
        self.ITEMS = Items()
        self.ITEMS.level_eight()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie,
            "-A-": Alien,
            "-B-": Boom
        }



class MapNine(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [170, 100, 100, 100, 70, 50, 30]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-", "-A-", "-B-", "-C-"]
        self.INTERACTIONS_COUNTER = [75, 32]
        self.INTERACTIONS = ["-|-", "-T-"]

        self.ITEMS = Items()
        self.ITEMS.level_nine()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie,
            "-A-": Alien,
            "-B-": Boom,
            "-C-": Chief
        }

  

class MapTen(Map):
    def get_values(self) -> None:
        self.MOPS_COUNTER = [270, 200, 200, 200, 170, 150, 130, 20]
        self.MOBS = ["-O-", "-L-", "-K-", "-Z-", "-A-", "-B-", "-C-", "-V-"]
        self.INTERACTIONS_COUNTER = [175, 52]
        self.INTERACTIONS = ["-|-", "-T-"]
        
        self.ITEMS = Items()
        self.ITEMS.level_ten()

        self.create_player_map()
        self.create_hidden_map(self.ITEMS.items_list, self.ITEMS.item_counter)

        self.generate_mob = {
            "-O-": Ork,
            "-L-": Lellek,
            "-K-": Kobold,
            "-Z-": Zombie,
            "-A-": Alien,
            "-B-": Boom,
            "-C-": Chief,
            "-V-": Villain
        }