from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.calculate_difficulty_level = self.calculate_difficulty_level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")

        self.__name = value

    @property
    def calculate_difficulty_level(self):
        return self.__calculate_difficulty_level

    @calculate_difficulty_level.setter
    def calculate_difficulty_level(self, value):
        self.__calculate_difficulty_level = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        if value < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")

        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self):
        pass
