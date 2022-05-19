from dataclasses import dataclass, field


@dataclass(slots=True)
class Items():
    items_list: list[str] = field(init=False)
    item_counter: list[int] = field(init=False)
    item_description: dict = field(init=False)

    def __post_init__(self):
        self.item_description = {
            "HP-": "A heal potion, which regenerate 100 health points",
            "AP-": "A attack potion, which boosts your attack by 100 points",
            "S?-": "It`s a sword with the level of the number, it boosts your attack depending on the level. You can only use one sword at the same time", 
            "A?-": "It`s armor with the level of the number, it decreases the damage from enemies depending on the level. You can only stack up to 7 at the same time",
            "RAA": "Reveal the area arround you -> 10x10",
            "RM-": "Reveal all monster on the map",
            "RD-": "Reveal the door",
            "RT-": "Reveal all traps",
            "HPF": "Heal potion, which heals you completely full",
            "RI-": "Reveal all items on the map",
            "KAM": "Kills all monster on the map",
            "SFM": "You can see the full map"
        }

    def level_one(self):
        self.items_list = ["HP-", "AP-", "S1-", "A1-"]
        self.item_counter = [2, 3, 1, 4]
    
    def level_two(self):
        self.items_list = ["HP-", "AP-", "S2-", "A2-"]
        self.item_counter = [4, 6, 2, 5]

    def level_three(self):
        self.items_list = ["HP-", "AP-", "S3-", "A3-", "RAA"]
        self.item_counter = [10, 12, 4, 10, 2]
    
    def level_four(self):
        self.items_list = ["HP-", "AP-", "S4-", "A4-", "RAA", "RM-"]
        self.item_counter = [20, 22, 10, 20, 8, 5]
    
    def level_five(self):
        self.items_list = ["HP-", "AP-", "S5-", "A5-", "RAA", "RM-", "RD-"]
        self.item_counter = [40, 32, 1, 40, 20, 8, 1]

    def level_six(self):
        self.items_list = ["HP-", "AP-", "S6-", "A6-", "RAA", "RM-", "RD-", "RT-"]
        self.item_counter = [60, 52, 4, 2, 12, 12, 4, 20]
    
    def level_seven(self):
        self.items_list = ["HP-", "AP-", "S7-", "A7-", "RAA", "RM-", "RD-", "RT-", "HPF"]
        self.item_counter = [50, 80, 5, 7, 22, 22, 14, 30, 20]

    def level_eight(self):
        self.items_list = ["HP-", "AP-", "S8-", "A8-", "RAA", "RM-", "RD-", "RT-", "HPF", "RI-"]
        self.item_counter = [60, 90, 15, 17, 42, 42, 24, 50, 30, 10]

    def level_nine(self):
        self.items_list = ["HP-", "AP-", "S9-", "A9-", "RAA", "RM-", "RD-", "RT-", "HPF", "RI-", "KAM"]
        self.item_counter = [60, 90, 15, 17, 42, 42, 24, 50, 30, 10, 1]

    def level_ten(self):
        self.items_list = ["HP-", "AP-", "S10", "A10", "RAA", "RM-", "RD-", "RT-", "HPF", "RI-", "KAM", "SFM"]
        self.item_counter = [99, 100, 1, 12, 44, 49, 44, 80, 50, 20, 10, 1]
