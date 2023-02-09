#!/usr/bin/python3
import random
from beverages import HotBeverage, Cappuccino, Chocolate, Tea, Coffee

def main():
    machine = CoffeeMachine()
    drinks = [Coffee, Tea, Cappuccino, HotBeverage, Chocolate]
    for i in range(0, 22):
        rand_drink = random.choice(drinks)
        try:
            print(machine.serve(rand_drink))
            print(f"Drinks Served: {machine.drinks_served}\n")
        except:
            print(machine.BrokenMachineException())
            machine.repair()

class CoffeeMachine():
    def __init__(self, drinks_served=0):
        self.drinks_served = drinks_served

    class EmptyCup(HotBeverage):
        def __init__(self, price=0.9, name="empty cup"):
            super().__init__(price, name)

        def description(self):
            return "An empty cup?! Gimme my money back!"

    def repair(self):
        self.drinks_served = 0

    def serve(self, drink):
        randomize = random.randrange(0, 2)
        if self.drinks_served == 10:
            raise self.BrokenMachineException()
        self.drinks_served += 1
        if randomize == 0:
            return drink()
        else:
            return self.EmptyCup()

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

if __name__ == "__main__":
    main()
