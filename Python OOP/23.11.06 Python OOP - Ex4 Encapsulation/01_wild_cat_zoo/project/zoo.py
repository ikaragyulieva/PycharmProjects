from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_to_pay = 0
        for worker in self.workers:
            total_to_pay += worker.salary

        if total_to_pay <= self.__budget:
            self.__budget -= total_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_care_budget = 0
        for animal in self.animals:
            total_care_budget += animal.money_for_care

        if total_care_budget <= self.__budget:
            self.__budget -= total_care_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            if animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            if animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        return '\n'.join([f"You have {len(self.animals)} animals"] +
                         [f"----- {len(lions)} Lions:"] + [f"{lion.__repr__()}" for lion in lions] +
                         [f"----- {len(tigers)} Tigers:"] + [f"{tiger.__repr__()}" for tiger in tigers] +
                         [f"----- {len(cheetahs)} Cheetahs:"] + [f"{cheetah.__repr__()}" for cheetah in cheetahs])

    def workers_status(self) -> str:
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            if worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            if worker.__class__.__name__ == "Vet":
                vets.append(worker)

        return '\n'.join([f"You have {len(self.workers)} workers"] +
                         [f"----- {len(keepers)} Keepers:"] + [f"{keeper.__repr__()}" for keeper in keepers] +
                         [f"----- {len(caretakers)} Caretakers:"] + [f"{taker.__repr__()}" for taker in caretakers] +
                         [f"----- {len(vets)} Vets:"] + [f"{vet.__repr__()}" for vet in vets])

