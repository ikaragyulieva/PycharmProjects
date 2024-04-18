from typing import List


class Account:
    def __init__(self, owner: str, amount=0, transactions=None) -> None:
        if transactions is None:
            transactions = list()
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = transactions

    def handle_transaction(self, transaction_amount: int):
        if self.amount + transaction_amount >= 0:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"
        else:
            raise ValueError("sorry cannot go in debt!")

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if self.amount + sum(self._transactions) + amount >= 0:
            self._transactions.append(amount)
            return f"New balance: {self.amount}"
        else:
            raise ValueError("sorry cannot go in debt!")

    @property
    def balance(self):
        transactions_sum = sum(self._transactions)
        return self.amount + transactions_sum

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __le__(self, other):
        return self.amount + sum(self._transactions) <= other.amount + sum(other._transactions)

    def __lt__(self, other):
        return self.amount + sum(self._transactions) < other.amount + sum(other._transactions)

    def __eq__(self, other):
        return self.amount + sum(self._transactions) == other.amount + sum(other._transactions)

    def __add__(self, other):
        return Account(f"{self.owner}&{other.owner}", self.amount + other.amount, self._transactions + other._transactions)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
