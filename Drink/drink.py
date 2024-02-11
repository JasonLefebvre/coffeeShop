class Drink:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def set_name(self, name):
        self.name = name
    
    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
class Soft(Drink): # Hérédite de Drink
    def __init__(self, name, price) -> None:
        super().__init__(name, price)

class Alcool(Drink): # Hérédite de Drink
    def __init__(self, name, price) -> None:
        super().__init__(name, price)