# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число N: '))
result = {}
summ_result = 0

for i in range(1, number+1):
    result[i] = round((1+1/i)**i, 2)
    summ_result += result[i]
print(f'N = {number}: {result}')
print(f'Сумма = {round(summ_result,3)}')
