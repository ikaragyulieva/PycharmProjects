# Create an abstract class called Vehicle that should have abstract methods drive and refuel.
# Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulate driving and refueling them.
# Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization.
# They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel).
# It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving is increased
# by 0.9 liters for the car and 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank,
# and when it is refueled, it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to
# its tank. If a vehicle cannot travel the given distance, its fuel does not change.
# Note: Submit all your classes and imports in the judge system

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @ abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    extra_fuel_consumption = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        ride_consumption = (self.fuel_consumption + Car.extra_fuel_consumption) * distance
        if self.fuel_quantity >= ride_consumption:
            self.fuel_quantity -= ride_consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    extra_fuel_consumption = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        ride_consumption = (self.fuel_consumption + Truck.extra_fuel_consumption) * distance
        if self.fuel_quantity >= ride_consumption:
            self.fuel_quantity -= ride_consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95


# Test1:
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
# 2.299999999999997
# 12.299999999999997

# Test2:
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
# 17.0
# 64.5
