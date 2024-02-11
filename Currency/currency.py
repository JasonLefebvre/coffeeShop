class Currency:

    def __init__(self, name:str = None, symbol:str = None) -> None:
        self.name = name
        self.symbol = symbol

    def set_name(self, name):
        self.name = name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol