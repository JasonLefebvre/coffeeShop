class Waiter:

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        pass

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name