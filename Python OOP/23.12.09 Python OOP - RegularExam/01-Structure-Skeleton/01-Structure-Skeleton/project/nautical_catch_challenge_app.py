from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DRIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISHES_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.VALID_DRIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        self.divers.append(self.VALID_DRIVER_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        self.fish_list.append(self.VALID_FISHES_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [diver for diver in self.divers if diver.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [fish for fish in self.fish_list if fish.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch and not is_lucky:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                count += 1
                diver.has_health_issue = False
                diver.renew_oxy()
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        try:
            diver = [diver for diver in self.divers if diver.name == diver_name][0]
        except IndexError:
            return

        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(fish.fish_details())

        return "\n".join(result)

    def competition_statistics(self):
        result = "**Nautical Catch Challenge Statistics**\n"
        healthy_divers = []
        for diver in self.divers:
            if not diver.has_health_issue:
                healthy_divers.append(diver)
        sorted_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result += "\n".join(str(diver) for diver in sorted_divers)
        return result
