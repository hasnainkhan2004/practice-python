#1
with open('newfile.txt', 'r') as file:
    print (file.read())
    
#2
with open('newfile.txt', 'r') as file:
    for x in file:
        print(x)