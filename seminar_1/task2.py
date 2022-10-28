# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1. 1, 4, 8, 7, 5 -> 8
# 2. 78, 55, 36, 90, 2 -> 90

# for
# my_list = []
# for i in [1,2,3,4,5]:
#     x = int(input('-->'))
#     my_list.append(x)

# print(my_list)

# range

# задать список с шагом
# my_list = []
# for i in range(10, 21, 2):
#     print(i)

# for + range + if
# maxx = 0
# for i in range(5):
#     x = int(input('-->'))
#     if i == 0:
#         maxx = x
#     elif x > maxx:
#         maxx = x

# print(maxx)

# while
my_listt = [5, 2, 9, 10, 3]
# i = 1
# maxxx = my_listt[0]
# while i < len(my_listt):
#     if my_listt[i] > maxxx:
#         maxxx = my_listt[i]
#     i += 1

# print(maxxx)

# перебор значений
for i in range(len(my_listt)):
    print(my_listt[i])


# Вариант 1
#a = int(input("Введите первое число"))
#b = int(input("Введите второе число"))
#c = int(input("Введите третье число"))
#d = int(input("Введите четвертое число"))
#e = int(input("Введите пятое число"))
#max_namber = a
# if max_namber < b:
#  max_namber = b
# if max_namber < c:
#  max_namber = c
# if max_namber < d:
#  max_namber = d
# if max_namber < e:
#  max_namber = e

#print(f"Максимальное число {max_namber}")


# Вариант 2
# my_list = [1, 4, 8, 7, 5]
# max_namber = my_list[0]
# i = 0
# while i < len(my_list):
#   if max_namber < my_list[i]:
#     max_namber = my_list[i]
#   i += 1

# print(f'{max_namber}')


# Вариант 3
# my_list1 = [1, 4, 8, 7, 5]
# my_list2 = [78, 55, 36, 90, 2]
# max_namber = my_list1[0]
# for i in my_list1:
#   if i > max_namber:
#     max_namber = i
# print(max_namber)


# Вариант 4 часто используется
# my_list1 = [1, 4, 8, 7, 5]
# my_list2 = [78, 55, 36, 90, 2]
# max_namber = my_list1[0]
# for i in range(len(my_list1)):
#   if my_list1[i] > max_namber:
#     max_namber = my_list1[i]
# print(max_namber)


# Вариант 5
# numbers = input()
# sorted_list = sorted(numbers)
# result = sorted_list[-1]
# print("Наибольшее число:", result)


# Вариант 6 доделать
# numbers = [1, 4, 8, 7, 5]
# my_list2 = [78, 55, 36, 90, 2]

# for i in numbers[0]
