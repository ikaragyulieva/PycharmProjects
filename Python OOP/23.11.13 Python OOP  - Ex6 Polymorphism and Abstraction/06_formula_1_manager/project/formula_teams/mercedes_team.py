from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        race_expenses = 200000
        prize = 0
        if race_pos == 1:
            prize = 1000000
        elif race_pos <= 3:
            prize = 500000
        if race_pos <= 5:
            prize += 100000
        elif race_pos <= 7:
            prize += 50000

        revenue = prize - race_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
