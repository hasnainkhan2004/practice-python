my_dic = {1:'Test', 'Name': 'Jim'}

print(my_dic[1])

my_dic[2] = 'Test 2'
print(my_dic)

my_dic[1] = 'Not a Test'
print(my_dic)

del my_dic[1]
print(my_dic)

for key, value in my_dic.items():
    print(str(key) + " : " + value)