#  1.	Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#  Пример: Для N = 5: 1, -3, 9, -27, 81


def func(x):
    a = 1
    for i in range(x):
        print(a, end=" ")
        a *= -3

func(5)

# Вариант 1
# Number_N = int(input("Введите число: "))

# for i in range (0, Number_N):
# print


# Вариант 2
# Number = int(input('Введите число N: '))

# result = []
# for degree in range(Number):
#     result.append(str((-3)**degree))

# print(", ".join(result), end=".")
