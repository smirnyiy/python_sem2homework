# Реализуйте алгоритм перемешивания списка.


import random

listRandom = [random.randint(0,11) for i in range(random.randint(1,21))]

print(f'Первоначальный рандомный список: {listRandom}\n')

random.shuffle(listRandom)

print(f'Финишный рандомный список после перемешивания: {listRandom}\n')