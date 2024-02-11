# Intéractions du serveur

from Customer.customer import Customer
from Drink.drink import *

def check_majority(customer:Customer):
    return customer.get_age < 18

def ask_drink():
    question = input("Bonjour, que voulez vous ? \n 1. Carte\n 2. Passer commande")
    if question == 1:
        print('Voici la carte')
    elif question == 2:
        order = input("Que commandez vous ?")
    return order

def give_drink(customer:Customer):
    pass

def ask_payment(customer:Customer, order:Drink):
    pass