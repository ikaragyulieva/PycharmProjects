from typing import Dict, Optional
from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int) -> None:
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str, float] = {}  # {topping_type: topping_weight}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value == "":
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self) -> Dough:
        return self.__dough

    @dough.setter
    def dough(self, value: Dough) -> None:
        if value is None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value

    @property
    def max_number_of_toppings(self) -> int:
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int) -> None:
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> None:
        if len(self.toppings) < self.max_number_of_toppings:
            if topping.topping_type not in self.toppings:
                self.toppings[topping.topping_type] = topping.weight
            else:
                self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self) -> float:
        total_weight = self.dough.weight + sum([w for w in self.toppings.values()])
        # for topping, weight in self.toppings.items():
        #     total_weight += weight

        return total_weight
