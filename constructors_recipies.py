class Recipie():
    def __init__(self, dish, items, time) -> None:# constructor method
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + " and takes " + str(self.time) + " min to prepare")

pizza = Recipie("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipie("Pasta", ["cheese", "sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())
print(pasta.contents())