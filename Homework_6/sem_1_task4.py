# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

x = float(input('->'))
x *= 10  # 6.78*10=67,8
x = int(x)  # int(67.8)=67
print(x % 10)  # 67%10=7


a = "6,78"
for i in range(len(a)):
    if a[i] == ',':
        print(a[i+1])

# from ctypes.wintypes import FLOAT


# b = 6.78
# res = ((b % 1) * 10) // 1
# print(b % 1)
# print(res)
# res = res // 1
# print(int(res))


# import math

# a = float(input('Введите число '))
# result_a = a * 10 % 10
# print(f'{int(result_a)}')

# n = FLOAT(input("Введите число n "))


# Решение преподавателя
# floatNum = float(input("Введите число с плавающей точкой: "))

# print(int(floatNum+10)%10)
