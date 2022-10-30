# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:

#  - [2, 3, 4, 5, 6] => [12, 15, 16]
#  - [2, 3, 5, 6] => [12, 15]

# что-то пошло не так
a = [2, 3, 4, 5, 6]
data = zip(a, a[len(a)-1])

# from random import randint
# import math

# def get_numbers(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 7
# first = 1
# last = 10

# mylist = get_numbers(n, first, last)
# print(mylist)
# print(mult_pairs(mylist))
