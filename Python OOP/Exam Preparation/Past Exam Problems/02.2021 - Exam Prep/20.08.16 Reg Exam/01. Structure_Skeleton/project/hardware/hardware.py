from typing import List
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        # available_memory =
        # available_capacity = self.capacity - sum([el.capacity_consumption for el in self.software_components])
        if software.capacity_consumption <= self.available_capacity and software.memory_consumption <= self.available_memory:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - sum([el.memory_consumption for el in self.software_components])

    @property
    def available_capacity(self):
        return self.capacity - sum([el.capacity_consumption for el in self.software_components])
