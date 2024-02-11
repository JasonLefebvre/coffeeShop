from Wallet.wallet import Wallet

class Customer:

    def __init__(self, name:str = None, age:int = None,  wallet:Wallet = None) -> None:
        self.name = name
        self.age = age
        self.wallet = wallet

    def set_name(self, name):
        self.name = name
        print(f"Ce client se nomme {self.name}")
    
    def set_wallet(self, wallet):
        self.wallet = wallet
        print(f"{self.name} a un wallet de {self.wallet.get_amount()} {self.wallet.get_currency()}")
    
    def set_age(self, age):
        self.age = age
        print(f"{self.name} est âgé de {self.age}")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_wallet(self):
        return self.wallet