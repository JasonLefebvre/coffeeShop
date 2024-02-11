from CoffeeShop.coffeeShop import CoffeeShop
from Currency.currency import Currency

def main():
    cafe = CoffeeShop()

    euro = Currency("Euro", "€")

    stock_base = {"café" : 10, "chococcino" : 10, "jus" : 10}

    cafe.set_name('ParisCofi')
    cafe.set_stock_quantity(stock_base)

    print(cafe.get_name())
    print(cafe.get_stock_quantity())
    cafe.serve("chococcino", 2)

main()