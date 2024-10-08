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
                if day < day_balance:
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
    balance_bob = Balance(200)
    balance_bob.add(
        Transaction(
            "Computer",
            -425.00, 
            datetime.datetime(2024, 1, 5)
        )
    )
    balance_bob.add(
        Transaction(
            "Gift",
            1000.00, 
            datetime.datetime(2024, 1, 10)
        )
    )
    balance_bob.add(
        Transaction(
            "Power",
            -220.00,
            datetime.datetime(2024, 2, 10),
            datetime.datetime(2024, 3, 10),
            "monthly"
        )
    )
    balance_bob.add(
        Transaction(
            "Profit",
            +49.50,
            datetime.datetime(2024, 1, 1),
            datetime.datetime(2024, 3, 31),
            "monthly"
        )
    )
    balance_bob.plot(
        datetime.datetime(2024, 1, 1),
        datetime.datetime(2024, 3, 31)
    )