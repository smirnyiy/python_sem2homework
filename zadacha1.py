# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


def FindSum(number):
    count = 0
    for i in number:
        if i.isdigit(): 
            count += int(i) 
    return count
digit = input("Введите число: ")
print(f"Сумма цифр вещественного числа - {digit} -> {FindSum(digit)}")