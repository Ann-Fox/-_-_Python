# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input('Введите число N -> '))
for i in range(-n, n+1):
    print(i, end=' ')


# import numbers

# number = int(input("Введите число"))
# a = number * -1

# while (a <= number):
#     print(a)
#     a += 1


# a = int(input('Введите число '))
# b = a * -1

# if a < b:
#     while a < b + 1:
#         print(f'{a}')
#         a += 1
# else:
#     while b < a + 1:
#         print(f'{b}')
#         b += 1


# n = int(input("Введите число N = "))
# s = ""
# for i in range(-n, n + 1):
#   # print(i, end=", ")
#   s += str(i) + ", "
# print(s[:-2])


# С использованием join соединяет список строк через знак-разделитель
# n = int(input("Введите число N = "))
# s = ""
# for i in range(-n, n + 1):
#   # print(i, end=", ")
#   s += str(i) + ", "
# print(s[:-2])


# n = int(input("Введите число N = "))
# s = []
# for i in range(-n, n + 1):
#     s.append(str(i))
# print(", ".join(s))


# Решение преподавателя
# N = int(input("Введите число N: "))

# listInt = []
# i = -N
# while i <= N:
    # listInt.append(i, end=", ")
#     listInt.append(str(i))
#     i += 1

# print(", ".join(listInt))
