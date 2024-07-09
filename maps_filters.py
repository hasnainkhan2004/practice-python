menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# map function 
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

# filter function
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
