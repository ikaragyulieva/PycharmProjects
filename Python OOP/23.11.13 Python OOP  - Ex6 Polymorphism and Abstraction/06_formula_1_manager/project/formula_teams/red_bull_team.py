from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        race_expenses = 250000
        prize = 0
        # if race_pos == 1:
        #     prize = 1500000
        # elif race_pos == 2:
        #     prize = 800000
        # if race_pos <= 8:
        #     prize += 20000
        # elif race_pos <= 10:
        #     prize += 10000

        # 2nd solution:
        sponsors = {"Oracle": {1: 1500000, 2: 800000},
                    "Honda": {8: 20000, 10: 10000}}
        for positions in sponsors.values():
            for position, money in positions.items():
                if race_pos <= position:
                    prize += money
                    break

        revenue = prize - race_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
