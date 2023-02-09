#!/usr/bin/python3

def main():
    hot_bev = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    choccy = Chocolate()
    cappuccino = Cappuccino()
    print(hot_bev)
    print(coffee)
    print(tea)
    print(choccy)
    print(cappuccino)

class HotBeverage():
    def __init__(self, price=0.3, name="hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        desc = f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"
        return desc 

    price = 0.30
    name = "hot beverage"

class Coffee(HotBeverage):
    def __init__(self, price=0.4, name="coffee"):
        super().__init__(price, name)

    def description(self):
        return "A coffee, to stay awake"

class Tea(HotBeverage):
    def __init__(self, price=0.3, name="tea"):
        super().__init__(price, name)

class Chocolate(HotBeverage):
    def __init__(self, price=0.5, name="chocolate"):
        super().__init__(price, name)

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self, price=0.45, name="cappuccino"):
        super().__init__(price, name)

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
    main()
