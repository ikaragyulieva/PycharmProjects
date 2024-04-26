from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)
        self.driver_type = "ScubaDiver"

    def miss(self, time_to_catch: int):
        if self.oxygen_level < time_to_catch * 0.3:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= round((time_to_catch * 0.3))
            if self.oxygen_level == 0:
                self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = 540
