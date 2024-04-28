
from project.climbers.base_climber import BaseClimber


class SummitClimber (BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)
        self.climber_type = "SummitClimber"

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak):
        if peak == "Advanced":
            self.strength -= (30 * 1.3)
        else:
            self.strength -= (30 * 2.5)
