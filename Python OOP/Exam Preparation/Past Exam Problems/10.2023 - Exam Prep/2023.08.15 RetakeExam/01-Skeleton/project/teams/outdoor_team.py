from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 1000.0)
        self.team_type = "OutdoorTeam"

    def win(self):
        self.advantage += 115
        self.wins += 1
