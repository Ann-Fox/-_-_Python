# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# c = 10

# if c % 10 == 0:
#   print("делится на 10")
# elif b == pow():
#   print("делится на 15")
# else:


#   numb = int(input())
# if numb % 5 and numb % 10 or numb % 15 or not numb % 30 :
#     print(True)
# else:
#     print(False)


# a = int(input('Введите число '))
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and not (a % 30 == 0):
#     print(f'кратно ')
# else:
#     print(f'не кратно ')


# Решение преподавателя
# from tokenize import Number

# Number = int(input("Введите число: "))

# if Number%10 == 0  or Number%15 == 0 and Number%30 != 0:
#     print("True")
# else:
#     print("False")


# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).

x = int(input('-->'))
if ((x % 5 == 0 and x % 10 == 0) or (x % 15 == 0 and x % 30 != 0)):
    print('yes')

