class Inventar():
    inventar_elements: list[str] = ["---" for _ in range(30)]
    inventar_gui: list[list[str]]

    def __init__(self) -> None:
        self.reload()

    @classmethod
    def remove_item(cls, item_pos: int) -> None:
        cls.inventar_elements[item_pos] = "---"
        cls.reload()


    @classmethod
    def add_item(cls, item: str) -> None:
        print(f"Add {item} to your inventar, if there is space left")
        for index, data in enumerate(cls.inventar_elements):
            if data == "---":
                cls.inventar_elements[index] = item
                cls.reload()
                break


    @classmethod
    def reload(cls) -> None:
        cls.inventar_gui = [
            ["-------------------------------------------------------------------------"],
            ["|", cls.inventar_elements[0], "|", cls.inventar_elements[1], "|", cls.inventar_elements[2], "|",
             cls.inventar_elements[3], "|", cls.inventar_elements[4], "|", cls.inventar_elements[5], "|"],
            ["|", "001", "|", "002", "|", "003", "|", "004", "|", "005", "|", "006", "|"],
            ["-------------------------------------------------------------------------"],
            ["|", cls.inventar_elements[6], "|", cls.inventar_elements[7], "|", cls.inventar_elements[8], "|",
             cls.inventar_elements[9], "|", cls.inventar_elements[10], "|", cls.inventar_elements[11], "|"],
            ["|", "007", "|", "008", "|", "009", "|", "010", "|", "011", "|", "012", "|"],
            ["-------------------------------------------------------------------------"],
            ["|", cls.inventar_elements[12], "|", cls.inventar_elements[13], "|", cls.inventar_elements[14], "|",
             cls.inventar_elements[15], "|", cls.inventar_elements[16], "|", cls.inventar_elements[17], "|"],
            ["|", "013", "|", "014", "|", "015", "|", "016", "|", "017", "|", "018", "|"],
            ["-------------------------------------------------------------------------"],
            ["|", cls.inventar_elements[18], "|", cls.inventar_elements[19], "|", cls.inventar_elements[20], "|",
             cls.inventar_elements[21], "|", cls.inventar_elements[22], "|", cls.inventar_elements[23], "|"],
            ["|", "019", "|", "020", "|", "021", "|", "022", "|", "023", "|", "024", "|"],
            ["-------------------------------------------------------------------------"],
            ["|", cls.inventar_elements[24], "|", cls.inventar_elements[25], "|", cls.inventar_elements[26], "|",
             cls.inventar_elements[27], "|", cls.inventar_elements[28], "|", cls.inventar_elements[29], "|"],
            ["|", "025", "|", "026", "|", "027", "|", "028", "|", "029", "|", "030", "|"],
            ["-------------------------------------------------------------------------"]
        ]
