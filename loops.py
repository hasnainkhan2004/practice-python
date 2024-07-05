#for loop
menu = ['apple','banana','orange','mango','peach']

for items in menu:
    print('I like this', items)

#while loop
menu = ['apple','banana','orange','mango','peach']

count=0
while count < len(menu):
    print('I like this', menu[count])
    count+=1

#using for loop showing index with value of item with in the array
menu = ['apple','banana','orange','mango','peach']

for idx,items in enumerate(menu):
    print(idx,items)
