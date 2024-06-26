from abc import ABC, abstractmethod


class BaseLoan(ABC):

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount
        self.loan_type = ""
        self.client_type = ""

    @abstractmethod
    def increase_interest_rate(self):
        pass
