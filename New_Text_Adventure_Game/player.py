from time import sleep


class Player():
    health_points: int = 100
    max_health: int = 100
    damage: int = 25
    armor: int = 0
    armor_list: list = []
    weapon: str = ""
    

    @classmethod
    def fight(cls, mob: object) -> bool:
        print(f"Your HP: {cls.health_points}\nYour damage: {cls.damage}\nYour armor: {cls.armor}\n{mob.NAME} HP: {mob.health_points}\n{mob.NAME} damage: {mob.DAMAGE}\n")
        while True:
            if mob.health_points <= 0 and cls.health_points > 0:
                return False
            
            elif cls.health_points <= 0:
                return True

            mob.health_points -= cls.damage
            cls.health_points -= mob.DAMAGE - cls.armor

            print(f"Your HP: {cls.health_points}\n{mob.NAME} HP: {mob.health_points}\n")
            sleep(2)

    
    @classmethod
    def change_values_by_item(cls, item: str) -> None:
        if item == "HP-":
            cls.health_points += 100
            if cls.health_points > cls.max_health:
                cls.max_health = cls.health_points

        elif item == "HPF":
            cls.health_points = cls.max_health
            
        elif item == "AP-":
            cls.damage += 100

        elif item  in ["S1-", "S2-", "S3-", "S4-", "S5-", "S6-", "S7-", "S8-", "S9-", "S10"]:
            if cls.weapon != "S10" and cls.weapon != "":
                cls.damage //= int(cls.weapon[1])* 2
            cls.damage *= int(item[1:2])* 2
            cls.weapon = item

        elif item  in ["A1-", "A2-", "A3-", "A4-", "A5-", "A6-", "A7-", "A8-", "A9-", "A10"]:
            if cls.armor == 0:
                cls.armor += 10

            if len(cls.armor_list) < 7:
                cls.armor_list.append(item)
                cls.armor *= int(item[1:2])* 2
                
            else:
                check_to_remove = [int(armor[1:2]) for armor in cls.armor_list]
                remove_value = min(check_to_remove)
                for i, d in enumerate(check_to_remove):
                    if d == remove_value:
                        cls.armor //= remove_value* 2
                        cls.armor_list[i] = item
                        cls.armor *= int(item[1:2])* 2
                        break