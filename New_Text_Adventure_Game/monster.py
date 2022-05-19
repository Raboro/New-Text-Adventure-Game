from dataclasses import dataclass, field


@dataclass(slots=True)
class Monster():
    DAMAGE: int = field(init=False)
    NAME: str = field(init=False)
    health_points: int = field(init=False)



@dataclass(slots=True)
class Ork(Monster): 
    def __post_init__(self) -> None:
        self.DAMAGE = 50
        self.NAME = "Ork"
        self.health_points = 100


@dataclass(slots=True)
class Lellek(Monster): 
    def __post_init__(self) -> None:
        self.DAMAGE = 70
        self.NAME = "Lellek"
        self.health_points = 120


@dataclass(slots=True)
class Kobold(Monster): 
    def __post_init__(self) -> None:
        self.DAMAGE = 40
        self.NAME = "Kobold"
        self.health_points = 50


@dataclass(slots=True)
class Zombie(Monster): 
    def __post_init__(self) -> None:
        self.DAMAGE = 20
        self.NAME = "Zombie"
        self.health_points = 240


@dataclass(slots=True)
class Alien(Monster):
    def __post_init__(self) -> None: 
        self.DAMAGE = 100
        self.NAME = "Alien"
        self.health_points = 300


@dataclass(slots=True)
class Boom(Monster):
    def __post_init__(self) -> None:
        self.DAMAGE = 100
        self.NAME = "Boom"
        self.health_points = 1000


@dataclass(slots=True)
class Chief(Monster):
    def __post_init__(self) -> None:
        self.DAMAGE = 222
        self.NAME = "Chief"
        self.healt_points = 1200


@dataclass(slots=True)
class Villain(Monster):
    def __post_init__(self) -> None:
        self.DAMAGE = 1000
        self.NAME = "Villain"
        self.health_points = 2000
