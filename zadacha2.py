# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def digit_factorial(num):
    array = [1]
    for i in range(1, num):
        array.append(array[i-1] * (i+1)) 
    return array
n = int(input("Введите число N: "))
print(f"Произведение чисел от 1 до {n} = {digit_factorial(n)}")



