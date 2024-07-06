def sum_of (**kwargs):
    sum = 0
    for x, y in kwargs.items():
        sum += y
    return round(sum, 2)

print (sum_of(cake=2.44, juice=5.25))