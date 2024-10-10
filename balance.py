import datetime
import matplotlib.pyplot as plt
from transaction import Transaction

class Balance():
    def __init__(self, balance_initial = 0) -> None:
        self.transactions = []
        self.balance_initial = balance_initial
        self.balance = balance_initial

    def add(self, transaction):
        self.transactions.append(transaction)

    def calculate_balance(self, day_balance):
        """Calculate the balance at the end of a day
        """
        self.balance = self.balance_initial
        for transaction in self.transactions:
            for day in transaction.days: 
                if day <= day_balance:
                    self.balance += transaction.value

        return self.balance

    def plot(self, day_start, day_end):
        dates = []
        balances = []

        current_date = day_start
        while current_date <= day_end:
            dates.append(current_date)
            balances.append(self.calculate_balance(
                current_date
            ))
            current_date += datetime.timedelta(days = 1)
            
        plt.figure(figsize=(10, 5))
        plt.plot(
            dates, 
            balances, 
            marker='o', 
            linestyle='None'
        )
        plt.xlabel('Day')
        plt.ylabel('Balance / EUR')
        plt.title('Balance as a function of the day')
        plt.grid(True)
        plt.show()

if "__main__" == __name__:
    balance_bob = Balance(500)
    balance_bob.add(
        Transaction(
            "Rent",
            -1.00, 
            datetime.datetime(2024, 11, 1),
            datetime.datetime(2025, 12, 1),
            "monthly"
        )
    )
    balance_bob.add(
        Transaction(
            "Income",
            10000000.00, 
            datetime.datetime(2024, 11, 1),
            datetime.datetime(2025, 12, 1),
            "monthly"
        )
    )
    balance_bob.plot(
        datetime.datetime(2024, 11, 1),
        datetime.datetime(2025, 6, 1)
    )