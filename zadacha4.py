# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input("Введите размер списка: ")) 
a = []

for i in range(N):  
    new_element = random.randint(-N, N)
    a.append(new_element)
print(f'Ваш список: {a}')

num = 1
with open('file.txt') as file:
    for pos in file:
        if int(pos) < N:
            num *= a[int(pos)]
        
print(num)