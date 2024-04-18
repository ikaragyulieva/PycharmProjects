from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    FOOD_EATEN = ['Vegetable', 'Fruit']
    WEIGHT_INCREMENT = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    FOOD_EATEN = ['Meat']
    WEIGHT_INCREMENT = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    FOOD_EATEN = ['Meat', 'Vegetable']
    WEIGHT_INCREMENT = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    FOOD_EATEN = ['Meat']
    WEIGHT_INCREMENT = 1

    def make_sound(self):
        return "ROAR!!!"
