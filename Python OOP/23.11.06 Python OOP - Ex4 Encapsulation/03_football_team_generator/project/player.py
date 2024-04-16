class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return '\n'.join([f"Player: {self.name}"] +
                         [f"Sprint: {self.__sprint}"] +
                         [f"Dribble: {self.__dribble}"] +
                         [f"Passing: {self.__passing}"] +
                         [f"Shooting: {self.__shooting}"])
