# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))

# print(bin(n)[2:])

# def binar(x):
#     return bin(n)[2:]

def calc(f, arg):
    print(f(arg))

calc(lambda x: bin(x)[2:], n)