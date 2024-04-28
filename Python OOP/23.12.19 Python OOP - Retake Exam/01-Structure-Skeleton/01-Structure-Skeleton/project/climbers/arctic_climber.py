

from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)
        self.climber_type = "ArcticClimber"

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak):
        if peak == "Extreme":
            self.strength -= (20 * 2)
        else:
            self.strength -= (20 * 1.5)
