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
        current_day = day_start
        while current_day < day_end:
            if interval == "monthly":
                if current_day.month < 12:
                    next_month = current_day.month + 1  
                    next_year = current_day.year
                else: 
                    next_month = 1
                    next_year = current_day.year + 1
                current_day = current_day.replace(
                    month=next_month, 
                    year=next_year
                )
                self.days.append(current_day)
    