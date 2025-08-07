from datetime import datetime

class Transaction:
    def __init__(self, category, amount, date=None):
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Date: {self.date}, Category: {self.category}, Amount: ₦{self.amount:.2f}"