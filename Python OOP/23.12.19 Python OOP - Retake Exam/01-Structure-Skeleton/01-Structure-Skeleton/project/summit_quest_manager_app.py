from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        for climber in self.climbers:
            if climber.name == climber_name:
                return f"{climber_name} has been already registered."

        self.climbers.append(self.VALID_CLIMBER_TYPES[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.VALID_PEAK_TYPES[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = [peak for peak in self.peaks if peak.name == peak_name][0]
        climber = [c for c in self.climbers if c.name == climber_name][0]
        missing_gears = []
        for g in peak.get_recommended_gear():
            if g not in gear:
                missing_gears.append(g)
        sorted_missing = []
        if missing_gears:
            climber.is_prepared = False
            sorted_missing = sorted(missing_gears)

        if climber.is_prepared:
            return f"{climber_name} is prepared to climb {peak_name}."
        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join([gear for gear in sorted_missing])}.")

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = [c for c in self.climbers if c.name == climber_name][0]
        except IndexError:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = [p for p in self.peaks if p.name == peak_name][0]
        except IndexError:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        elif not climber.can_climb():
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak.calculate_difficulty_level())
        climber.conquered_peaks.append(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."

    def get_statistics(self):
        climbed_peaks = []
        for c in self.climbers:
            for p in c.conquered_peaks:
                if p not in climbed_peaks:
                    climbed_peaks.append(p)

        successful_climbers = [c for c in self.climbers if c.conquered_peaks]
        sorted_successful_climbers = sorted(successful_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        result = [f"Total climbed peaks: {len(climbed_peaks)}", "**Climber's statistics:**"]
        for c in sorted_successful_climbers:
            result.append(c.__str__())

        return '\n'.join(result)
