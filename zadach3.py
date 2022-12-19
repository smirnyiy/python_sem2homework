# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# Для n=6 [2,2,2,2,2,2] -> 13

num = int(input('Введите число N: '))
sum_nums = 0
list_nums = []
for i in range(1, num + 1):           
    result = round((1 + 1 / i) ** i)  
                                      
    list_nums.append(result)
    sum_nums += result

print(f"{list_nums} -> {sum_nums}")



