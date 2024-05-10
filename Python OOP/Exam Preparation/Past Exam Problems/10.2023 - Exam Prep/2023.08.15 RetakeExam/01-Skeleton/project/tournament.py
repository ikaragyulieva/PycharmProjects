from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"ElbowPad": ElbowPad, "KneePad": KneePad}
    VALID_TEAM_TYPES = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # if not re.match("^[A-Za-z0-9]", value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    # def add_equipment(self, equipment_type: str):
    #     if equipment_type == "KneePad":
    #         self.equipment.append(KneePad())
    #         return f"{equipment_type} was successfully added."
    #     elif equipment_type == "ElbowPad":
    #         self.equipment.append(ElbowPad())
    #         return f"{equipment_type} was successfully added."
    #     else:
    #         raise Exception("Invalid equipment type!")

    # 2nd solution add equipment method
    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    # 2nd solution add team method
    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    # def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
    #     if team_type == "OutdoorTeam":
    #         if self.capacity == len(self.teams):
    #             return "Not enough tournament capacity."
    #         self.teams.append(OutdoorTeam(team_name, country, advantage))
    #         return f"{team_type} was successfully added."
    #     elif team_type == "IndoorTeam":
    #         if self.capacity == len(self.teams):
    #             return "Not enough tournament capacity."
    #         self.teams.append(IndoorTeam(team_name, country, advantage))
    #         return f"{team_type} was successfully added."
    #     else:
    #         raise Exception("Invalid team type!")

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [eq for eq in reversed(self.equipment) if eq.equipment_type == equipment_type][0]
        team = [t for t in self.teams if t.name == team_name][0]

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = [t for t in self.teams if t.name == team_name][0]
        except IndexError:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for eq in self.equipment:
            if eq.equipment_type == equipment_type:
                count += 1
                eq.increase_price()

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_one = [t for t in self.teams if t.name == team_name1][0]
        team_two = [t for t in self.teams if t.name == team_name2][0]

        if team_one.team_type != team_two.team_type:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_score = team_one.advantage + sum([eq.protection for eq in team_one.equipment])
        team_two_score = team_two.advantage + sum([eq.protection for eq in team_two.equipment])
        winner = team_one if team_one_score > team_two_score else team_two if team_two_score > team_one_score else None

        if winner is None:
            return "No winner in this game."
        winner.win()
        return f"The winner is {winner.name}."
        #
        # if team_one_score > team_two_score:
        #     team_one.win()
        #     return f"The winner is {team_name1}."
        # elif team_two_score > team_one_score:
        #     team_two.win()
        #     return f"The winner is {team_name2}."
        # else:
        #     return "No winner in this game."

    def get_statistics(self):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"]
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        for team in sorted_teams:
            result.append(team.get_statistics())

        return "\n".join(result)
