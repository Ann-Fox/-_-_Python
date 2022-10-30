# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1*1, 1*2, 1*2*3, 1*2*3*4)

import math

number = int(input("Введите число: "))

li = [x for x in range(1, number+1)]
print(li)
li = list(map(lambda x: math.factorial(x), li))
print(li)

# factorial = 1
# list_factorial = []
# for i in range(1, number+1):
#     factorial *=i
#     list_factorial.append(factorial)
# print(f'N = {number}, тогда факториал {list_factorial}')
# print()