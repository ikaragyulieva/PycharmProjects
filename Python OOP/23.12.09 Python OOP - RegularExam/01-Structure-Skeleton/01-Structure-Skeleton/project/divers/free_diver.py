from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 120)
        self.driver_type = "FreeDiver"

    def miss(self, time_to_catch: int):
        if self.oxygen_level < time_to_catch * 0.6:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= round(time_to_catch * 0.6)
            if self.oxygen_level == 0:
                self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = 120



