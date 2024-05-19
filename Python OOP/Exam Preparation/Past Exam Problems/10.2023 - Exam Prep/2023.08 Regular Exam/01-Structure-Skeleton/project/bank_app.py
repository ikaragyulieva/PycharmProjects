from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        self.loans.append(self.VALID_LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = [loan for loan in self.loans if loan.loan_type == loan_type][0]
        client = [c for c in self.clients if c.client_id == client_id][0]
        if client.client_type != loan.client_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        for loan in self.loans:
            if loan.loan_type == loan_type:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        result = [f"Active Clients: {len(self.clients)}"]
        total_income = 0
        granted_loans = 0
        sum_granted_loans = 0
        clients_interest = 0
        for client in self.clients:
            total_income += client.income
            granted_loans += len(client.loans)
            clients_interest += client.interest

            for loan in client.loans:
                sum_granted_loans += loan.amount

        avg_client_interest_rate = (clients_interest/len(self.clients)) if clients_interest else 0

        result.append(f"Total Income: {total_income:.2f}")
        result.append(f"Granted Loans: {granted_loans}, Total Sum: {sum_granted_loans:.2f}")
        result.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum([loan.amount for loan in self.loans]):.2f}")
        result.append(f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
        return "\n".join(result)
