from Drink.drink import Drink

class CoffeeShop:

    States = ["open", "restocking", "closed"]

    def __init__(self, name:str = None, stock_quatity:dict[Drink][int] = None) -> None:
        self.name = name
        self.stock_quatity = stock_quatity
        self.state = None

    def __str__(self) -> str:
        return f"name : {self.name} - stock: {self.stock_quatity}"

    def get_name(self):
        return self.name
    
    def get_stock_quantity(self):
        return self.stock_quatity
    
    def open(self):
        self.state = CoffeeShop.States[0]
        print(f"Le {self.name} ouvre")

    def close(self):
        self.state = CoffeeShop.States[2]
        print(f"Le {self.name} ferme")

    def get_state(self):
        return self.state
    
    def set_name(self, name):
        self.name = name
        print(f"Votre café se nomme à présent {self.name}")

    def set_stock_quantity(self, stock):
        self.stock_quatity = stock
        print(f"Votre café contient un stock de : {self.stock_quatity}")
    
    def serve(self, drink, quantity):
        self.stock_quatity[drink] -= quantity
        print(f"Tiens mec, voilà tes {quantity} boisson(s) : {drink}")
    
    def renew_stock(self, drink, quantity):
        self.state = CoffeeShop.States[1]
        self.stock_quatity[drink] += quantity
        print(f"Stock réapprovisionné de {quantity} {drink}")