import datetime

class Transaction():
    def __init__(
        self, 
        id, 
        value, 
        day, 
        day_end = None,
        interval = "daily") -> None:

        self.id = id
        # [EUR]
        # + <=> Inbound
        # - <=> Outbound
        self.value = value
        # Day, month, year
        self.days = [day]
        self.interval = interval
        if self.interval == "monthly":
            self.calculate_dates(
                day, 
                day_end, 
                self.interval
            )
        elif self.interval == "daily":
            self.set_day(day)

    def set_day(self, day):
        self.days = [day]

    def calculate_dates(
        self, 
        day_start, 
        day_end, 
        interval):
        """Calculate the days of the transaction
        """
        current_date = day_start
        while current_date <= day_end:
            self.days.append(current_date)
            if interval == "monthly":
                next_month = current_date.month + 1 if current_date.month < 12 else 1
                next_year = current_date.year if current_date.month < 12 else current_date.year + 1
                current_date = current_date.replace(month=next_month, year=next_year)
    