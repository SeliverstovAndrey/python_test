import random

str1 = input('Enter the string: ')
str2 = set(str1.replace(' ',''))
print(str2)

rand = int(random.randint(0, len(str2) - 1))
print(rand)

el = list(str2)
print('Random symbol is: ',el[rand])
