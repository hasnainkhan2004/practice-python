def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]#sliced version used
# (str[1:])the slicing removes the first character from the string
# (str[1:]). The slicing removes the first character from the string    

str = "reversal"
reverse = string_reverse(str)
print(reverse)