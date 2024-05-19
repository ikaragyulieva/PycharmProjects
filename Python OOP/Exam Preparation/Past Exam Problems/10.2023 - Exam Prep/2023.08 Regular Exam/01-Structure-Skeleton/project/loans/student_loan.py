from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self):
        super().__init__(1.5, 2000.0)
        self.loan_type = "StudentLoan"
        self.client_type = "Student"

    def increase_interest_rate(self):
        self.interest_rate += 0.2
