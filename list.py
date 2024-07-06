list1 = [1, 2, 3, 4, 5]

print (*list1)
print (list1)

list1.pop(4)
print (list1)

del list1 [2]
print (list1)

list1.append(6)
print (list1)

list1.extend([6, 7, 8])
print (list1)

for x in list1:
    print('Value:', list1)