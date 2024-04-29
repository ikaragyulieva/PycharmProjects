from typing import List
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append((HeavyHardware(name, capacity, memory)))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            s = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(s)
            System._software.append(s)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            s = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(s)
            System._software.append(s)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: " \
               f"{sum(m.memory_consumption for m in System._software)} / {sum(m.memory for m in System._hardware)}\n" \
               f"Total Capacity Taken: " \
               f"{sum(c.capacity_consumption for c in System._software)} / {sum(c.capacity for c in System._hardware)}"

    @staticmethod
    def system_split():
        return '\n'.join([
            f"Hardware Component - {h.name}\n"
            f"Express Software Components: {sum(1 for s in h.software_components if s.software_type == 'Express')}\n"
            f"Light Software Components: {sum(1 for s in h.software_components if s.software_type == 'Light')}\n"
            f"Memory Usage: {sum(s.memory_consumption for s in h.software_components)} / {h.memory}\n"
            f"Capacity Usage: {sum(s.capacity_consumption for s in h.software_components)} / {h.capacity}\n"
            f"Type: {h.hardware_type}\n"
            f"Software Components: " f"{', '.join(s.name for s in h.software_components) if h.software_components else 'None'}"
            for h in System._hardware])
