from Currency.currency import Currency

class Wallet:
    
    def __init__(self, amount:int = None, currency:Currency = None) -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f"Wallet -> {self.amount} {self.currency}"
    
    def set_amount(self, amount):
        self.amount = amount
    
    def set_currency(self, currency):
        self.currency = currency

    def get_amount(self):
        return self.amount
    
    def get_currency(self):
        return self.currency
    
    def add_money(self, amount, currency):
        if currency == self.get_currency():
            self.amount += amount
        else:
            return "Mauvaise devise"
    
    def remove_money(self, amount, currency):
        if currency == self.get_currency():
            self.amount -= amount
        else:
            return "Mauvaise devise"