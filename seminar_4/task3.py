# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# один из часто используемых в математике способов — это нахождение НОК при помощи разложения чисел на простые множители. В общем случае алгоритм будет выглядеть следующим образом:
# 1. разложить оба числа на простые множители;
# 2. выбрать одну группу множителей;
# 3. добавить к ним множители из второй группы, которые отсутствуют в выбранной;
# 4. найти их произведение.




def find(a, b):

    if a > b:
        max_num = a
        min_num = b
    else:
        max_num = b
        min_num = a

    for i in range(2, min_num):
        if min_num % i == 0 and max_num % i == 0:
            return i


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
nok = find(a, b)
print(nok)
