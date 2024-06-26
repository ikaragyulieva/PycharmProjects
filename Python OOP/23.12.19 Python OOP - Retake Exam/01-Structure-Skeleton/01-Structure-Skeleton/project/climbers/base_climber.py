from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[BasePeak] = []
        self.is_prepared: bool = True
        self.climber_type = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")

        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return (f"{self.climber_type}: /// "
                f"Climber name: {self.name} * "
                f"Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {', '.join([el.name for el in sorted(self.conquered_peaks, key=lambda x: x.name)])} ///")
